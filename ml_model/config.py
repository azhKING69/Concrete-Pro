# ml_model/config.py
# This is the master config file for all ML and engineering logic.

import numpy as np

# --- 1. CONFIG FOR RECOMMENDER (Page 2) ---

# Prices for recommender's cost calculation
RECOMMENDER_MATERIAL_PRICES = {
    "cement": 7.5,
    "sand": 1.5,
    "coarse_agg": 1.5,
}

# The design-mix table for the Recommender page
DESIGN_MIX_TABLE = {
    'M5': {'cement': 160, 'wc': 0.60, 'water': 96, 'sand': 800, 'coarse_agg': 1200, 'admixture': 0.5},
    'M7.5': {'cement': 180, 'wc': 0.60, 'water': 108, 'sand': 760, 'coarse_agg': 1240, 'admixture': 0.5},
    'M10': {'cement': 200, 'wc': 0.58, 'water': 116, 'sand': 722, 'coarse_agg': 1228, 'admixture': 0.5},
    'M15': {'cement': 240, 'wc': 0.52, 'water': 125, 'sand': 684, 'coarse_agg': 1216, 'admixture': 0.5},
    'M20': {'cement': 300, 'wc': 0.45, 'water': 135, 'sand': 702, 'coarse_agg': 1098, 'admixture': 0.5},
    'M25': {'cement': 350, 'wc': 0.42, 'water': 147, 'sand': 682, 'coarse_agg': 1068, 'admixture': 0.5},
    'M30': {'cement': 400, 'wc': 0.40, 'water': 160, 'sand': 700, 'coarse_agg': 1050, 'admixture': 0.6},
    'M35': {'cement': 410, 'wc': 0.38, 'water': 156, 'sand': 718, 'coarse_agg': 1032, 'admixture': 0.6},
    'M40': {'cement': 420, 'wc': 0.36, 'water': 151, 'sand': 714, 'coarse_agg': 986, 'admixture': 0.8},
    'M45': {'cement': 440, 'wc': 0.34, 'water': 150, 'sand': 731, 'coarse_agg': 969, 'admixture': 0.8},
    'M50': {'cement': 450, 'wc': 0.32, 'water': 144, 'sand': 739, 'coarse_agg': 941, 'admixture': 1.0},
    'M55': {'cement': 460, 'wc': 0.30, 'water': 138, 'sand': 742, 'coarse_agg': 908, 'admixture': 1.0},
    'M60': {'cement': 470, 'wc': 0.28, 'water': 132, 'sand': 759, 'coarse_agg': 891, 'admixture': 1.2},
    'M65': {'cement': 480, 'wc': 0.27, 'water': 130, 'sand': 766, 'coarse_agg': 864, 'admixture': 1.2},
    'M70': {'cement': 490, 'wc': 0.26, 'water': 127, 'sand': 778, 'coarse_agg': 842, 'admixture': 1.5},
    'M75': {'cement': 500, 'wc': 0.25, 'water': 125, 'sand': 784, 'coarse_agg': 816, 'admixture': 1.5},
    'M80': {'cement': 510, 'wc': 0.24, 'water': 122, 'sand': 800, 'coarse_agg': 800, 'admixture': 1.8},
    'M90': {'cement': 520, 'wc': 0.23, 'water': 120, 'sand': 806, 'coarse_agg': 774, 'admixture': 2.0},
    'M100': {'cement': 540, 'wc': 0.22, 'water': 119, 'sand': 806, 'coarse_agg': 744, 'admixture': 2.5},
}


# --- 2. CONFIG FOR OPTIMIZER (Page 3) ---

# Prices for the 3 materials the optimizer will vary
OPTIMIZER_MATERIAL_PRICES = {
    "cement": 7.5,
    "coarse_aggregate": 1.5,
    "fine_aggregate": 1.5,
}

# The 3 features the optimizer will vary.
OPTIMIZABLE_FEATURES = [
    'cement',
    'coarse_aggregate',
    'fine_aggregate'
]

# Bounds for the 3 optimizable materials (kg/m³)
OPTIMIZER_BOUNDS = [
    (250, 550),  # Cement
    (800, 1200), # Coarse Aggregate
    (600, 950)   # Fine Aggregate
]

# Water-Cement Ratio Table (based on IS 456)
# Filled in for all grades
WC_RATIO_TABLE = {
    5: (0.60, 0.60, 0.60), 7.5: (0.60, 0.60, 0.60),
    10: (0.58, 0.55, 0.50), 15: (0.52, 0.50, 0.45),
    20: (0.55, 0.50, 0.45), 25: (0.55, 0.50, 0.45),
    30: (0.50, 0.45, 0.40), 35: (0.45, 0.40, 0.40),
    40: (0.45, 0.40, 0.40), 45: (0.40, 0.35, 0.35),
    50: (0.40, 0.35, 0.35), 55: (0.35, 0.35, 0.35),
    60: (0.35, 0.35, 0.35), 65: (0.35, 0.35, 0.35),
    70: (0.35, 0.35, 0.35), 75: (0.35, 0.35, 0.35),
    80: (0.35, 0.35, 0.35), 90: (0.35, 0.35, 0.35),
    100: (0.35, 0.35, 0.35)
}

# Standard deviation values (based on IS 10262:2019 Table 2)
# Filled in for all grades
STANDARD_DEVIATION_TABLE = {
    5: 3.5, 7.5: 3.5, 10: 3.5, 15: 3.5,
    20: 4.0, 25: 4.0,
    30: 5.0, 35: 5.0, 40: 5.0, 45: 5.0, 50: 5.0, 55: 5.0,
    60: 5.0, 65: 5.0, 70: 5.0, 75: 5.0, 80: 5.0, 90: 5.0, 100: 5.0
}