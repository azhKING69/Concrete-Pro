# ml_model/optimize.py
# FINAL VERSION: Fixes a key inconsistency in the fallback logic.

import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, Bounds
from ml_model.predict import predict_strength 
from ml_model.recommender import get_mix_recommendation
from ml_model.config import (
    OPTIMIZER_MATERIAL_PRICES, OPTIMIZABLE_FEATURES, OPTIMIZER_BOUNDS, 
    WC_RATIO_TABLE, STANDARD_DEVIATION_TABLE, DESIGN_MIX_TABLE
)

def cost_function(proportions_to_optimize):
    cost = 0.0
    for i, material_name in enumerate(OPTIMIZABLE_FEATURES):
        cost += proportions_to_optimize[i] * OPTIMIZER_MATERIAL_PRICES[material_name]
    return float(cost)

def get_wc_ratio(target_strength):
    strength_key = min(WC_RATIO_TABLE.keys(), key=lambda k: abs(k - target_strength))
    return WC_RATIO_TABLE[strength_key][1] # Default to Moderate exposure

def run_optimizer(characteristic_strength, fixed_slag, fixed_fly_ash, fixed_superplasticizer):
    """
    Runs the final, smart hybrid optimization process.
    """
    
    # --- STEP 1: Find the closest standard grade to the user's input ---
    table_grades = {int(g.replace('M','')): g for g in DESIGN_MIX_TABLE.keys() if g.replace('M','').isdigit()}
    closest_grade_val = min(table_grades.keys(), key=lambda k: abs(k - characteristic_strength))
    baseline_grade_str = table_grades[closest_grade_val]
    
    baseline_mix = get_mix_recommendation(baseline_grade_str)
    
    if not baseline_mix:
        return {"success": False, "message": f"Could not find a baseline mix for target {characteristic_strength} MPa."}

    # --- STEP 2: Use the baseline to run the ML fine-tuning for the EXACT target ---
    std_dev_key = min(STANDARD_DEVIATION_TABLE.keys(), key=lambda k: abs(k - characteristic_strength))
    std_dev = STANDARD_DEVIATION_TABLE[std_dev_key]
    target_mean_strength = characteristic_strength + (1.65 * std_dev) # Use exact target here
    max_wc_ratio = get_wc_ratio(characteristic_strength)
    age = 28.0

    def strength_constraint_fun(proportions_to_optimize):
        cement, coarse_agg, fine_agg = proportions_to_optimize
        water = max_wc_ratio * cement
        raw_features_list = [
            cement, fixed_slag, fixed_fly_ash, water, fixed_superplasticizer,
            coarse_agg, fine_agg, age
        ]
        predicted_strength = predict_strength(raw_features_list)
        return float(predicted_strength)

    nonlinear_constraint = NonlinearConstraint(strength_constraint_fun, target_mean_strength, np.inf)
    constraints = [nonlinear_constraint]
    
    lower_bounds = [b[0] for b in OPTIMIZER_BOUNDS]
    upper_bounds = [b[1] for b in OPTIMIZER_BOUNDS]
    bounds = Bounds(lower_bounds, upper_bounds)
    
    initial_guess = [
        baseline_mix['quantities_kg']['Cement'],
        baseline_mix['quantities_kg']['Coarse Aggregate'],
        baseline_mix['quantities_kg']['Sand (Fine Aggregate)'],
    ]

    result = minimize(
        cost_function, initial_guess, method='trust-constr',
        bounds=bounds, constraints=constraints, options={'disp': False, 'maxiter': 1000}
    )

    # --- STEP 3: Return the ML-tuned result or the reliable baseline as a fallback ---
    if result.success:
        cement, coarse_agg, fine_agg = result.x
        final_cost = result.fun
        final_water = max_wc_ratio * cement
        final_features = [cement, fixed_slag, fixed_fly_ash, final_water, fixed_superplasticizer, coarse_agg, fine_agg, age]
        final_strength = predict_strength(final_features)
        
        final_mix_kg = {"Cement": cement, "Water": final_water, "Fine Aggregate": fine_agg, "Coarse Aggregate": coarse_agg}
        mix_ratio = {"Cement": 1, "Water": final_water / cement, "Fine Aggregate": fine_agg / cement, "Coarse Aggregate": coarse_agg / cement}
        
        return {
            "success": True, "was_fine_tuned": True, "cost": final_cost, 
            "predicted_strength": final_strength, "target_mean_strength": target_mean_strength,
            "mix_kg": final_mix_kg, "mix_ratio": mix_ratio, "wc_ratio_used": max_wc_ratio
        }
    else:
        # --- THE FALLBACK ---
        baseline_kg = {
            "Cement": baseline_mix['quantities_kg']['Cement'], "Water": baseline_mix['quantities_kg']['Water'],
            "Fine Aggregate": baseline_mix['quantities_kg']['Sand (Fine Aggregate)'],
            "Coarse Aggregate": baseline_mix['quantities_kg']['Coarse Aggregate']
        }
        
        # FIX: Reconstruct the mix_ratio dictionary to ensure consistent keys
        reconstructed_mix_ratio = {
            "Cement": 1,
            "Water": baseline_mix['mix_ratio']['Water'],
            "Fine Aggregate": baseline_mix['mix_ratio']['Sand'], # Map 'Sand' to 'Fine Aggregate'
            "Coarse Aggregate": baseline_mix['mix_ratio']['Coarse Aggregate']
        }

        return {
            "success": True, "was_fine_tuned": False, "cost": baseline_mix['cost'], 
            "predicted_strength": characteristic_strength, "target_mean_strength": target_mean_strength,
            "mix_kg": baseline_kg, 
            "mix_ratio": reconstructed_mix_ratio, # Return the consistent dictionary
            "wc_ratio_used": baseline_mix['quantities_kg']['Water'] / baseline_mix['quantities_kg']['Cement']
        }

