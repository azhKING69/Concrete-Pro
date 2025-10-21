# ml_model/feature_engineering.py
# This module contains the logic to transform the 8 raw inputs
# from the web form into the 6 features the model expects.

import numpy as np

def transform_features(raw_features_list):
    """
    Transforms 8 raw input features into the 6 engineered features.

    Args:
        raw_features_list (list): A list of 8 features in the order:
        [Cement, Slag, Fly Ash, Water, Superplasticizer, 
         Coarse Agg, Fine Agg, Age]

    Returns:
        numpy.ndarray: A numpy array with the 6 engineered features:
        [binder, aggregate, Water, Superplasticizer, Age]
    """
    # Convert to a numpy array for easier calculations
    features = np.array(raw_features_list)

    # Indices from the raw feature list
    cement = features[0]
    slag = features[1]
    fly_ash = features[2]
    water = features[3]
    superplasticizer = features[4]
    coarse_agg = features[5]
    fine_agg = features[6]
    age = features[7]

    # Perform the same feature engineering as in the notebook
    binder = cement + slag + fly_ash
    aggregate = coarse_agg + fine_agg

    # Return the 6 features in the correct order the model was trained on
    return np.array([binder, aggregate, water, superplasticizer, age])
