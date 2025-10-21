# ml_model/recommender.py
# This file contains the logic for the Design-Mix Recommender.

# The import is now correct
from ml_model.config import DESIGN_MIX_TABLE, RECOMMENDER_MATERIAL_PRICES

def get_mix_recommendation(grade):
    """
    Looks up a concrete grade in the design-mix table and calculates cost and ratios.
    """
    
    # 1. Look up the mix details from the table
    mix_data = DESIGN_MIX_TABLE.get(grade)
    
    if not mix_data:
        return None # Grade not found in our table

    # 2. Extract quantities
    cement = mix_data['cement']
    water = mix_data['water']
    sand = mix_data['sand']
    coarse_agg = mix_data['coarse_agg']
    
    # 3. Calculate the estimated cost using the correct variable name
    cost = (
        cement * RECOMMENDER_MATERIAL_PRICES['cement'] +
        sand * RECOMMENDER_MATERIAL_PRICES['sand'] +
        coarse_agg * RECOMMENDER_MATERIAL_PRICES['coarse_agg']
    )

    # 4. Calculate the final mix ratio (dividing all by cement)
    mix_ratio = {
        "Cement": 1,
        "Water": water / cement,
        "Sand": sand / cement,
        "Coarse Aggregate": coarse_agg / cement
    }

    # 5. Return everything in a structured dictionary
    return {
        "grade": grade,
        "cost": cost,
        "quantities_kg": {
            "Cement": cement,
            "Water": water,
            "Sand (Fine Aggregate)": sand,
            "Coarse Aggregate": coarse_agg
        },
        "admixture_percentage": mix_data['admixture'],
        "mix_ratio": mix_ratio,
    }

