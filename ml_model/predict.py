# ml_model/predict.py
# This module now orchestrates the full prediction pipeline:
# 1. Transforms raw inputs using feature_engineering.
# 2. Scales the engineered features using the saved scaler.
# 3. Makes a prediction using the saved model.

import joblib
import numpy as np
import os
from ml_model.feature_engineering import transform_features # <-- IMPORT NEW FUNCTION

# --- Load Model and Scaler ---
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'saved_model/concrete_strength_model.pkl')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'saved_model/scaler.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH) # <-- LOAD THE SCALER
except FileNotFoundError as e:
    raise FileNotFoundError(
        f"Model or scaler file not found. Please run the training script and place "
        "'concrete_strength_model.pkl' and 'scaler.pkl' in the 'ml_model/saved_model/' directory."
    ) from e

def predict_strength(raw_features_list):
    """
    Predicts concrete strength from a list of 8 raw features.
    
    Args:
        raw_features_list (list): A list of 8 raw feature values.
    
    Returns:
        float: The predicted compressive strength.
    """
    
    # 1. Transform the 8 raw features into 6 engineered features
    engineered_features = transform_features(raw_features_list)
    
    # 2. Reshape for the scaler (it expects a 2D array)
    engineered_features_reshaped = engineered_features.reshape(1, -1)
    
    # 3. Scale the engineered features using the loaded scaler
    scaled_features = scaler.transform(engineered_features_reshaped)
    
    # 4. Make the prediction on the scaled, engineered features
    prediction = model.predict(scaled_features)
    
    # 5. Return the result
    return round(prediction[0], 2)