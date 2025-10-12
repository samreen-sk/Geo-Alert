from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- add this import
import joblib
import numpy as np
import pandas as pd


# Step 1: Create Flask app
app = Flask(__name__)
CORS(app)
# Step 2: Load saved models and scaler
rf_model = joblib.load('rf_classifier.pkl')
rf_reg = joblib.load('rf_regressor.pkl')
log_model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Step 3: Define /predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Step 3a: Convert JSON into DataFrame
        df = pd.DataFrame([data])
        
        # Step 3b: Check columns
        expected_columns = [
            "Rainfall_mm","Rainfall_3Day","Rainfall_7Day","Aspect","Elevation_m",
            "NDVI_Index","Land_Use_Urban","Land_Use_Forest","Land_Use_Agriculture",
            "Earthquake_Activity","Proximity_to_Water","Distance_to_Road_m",
            "Temperature_C","Humidity_percent","Soil_pH","Clay_Content","Sand_Content",
            "Silt_Content","Soil_Erosion_Rate","Historical_Landslide_Count",
            "Soil_Type_Gravel","Soil_Type_Sand","Soil_Type_Silt","Soil_Type_Clay",
            "Pore_Water_Pressure_kPa","Soil_Moisture_Content","Microseismic_Activity",
            "Acoustic_Emission_dB","Soil_Strain","Soil_Temperature_C","TDR_Reflection_Index"
        ]
        
        # Ensure columns are in correct order
        df = df[expected_columns]
        
        # Step 3c: Scale features for logistic regression
        X_scaled = scaler.transform(df)
        
        # Step 3d: Predictions
        rf_pred = rf_model.predict(df)
        rf_reg_pred = rf_reg.predict(df)
        log_pred = log_model.predict(X_scaled)
        
        # Step 3e: Return JSON
        return jsonify({
            "rf_prediction": rf_pred.tolist(),
            "rf_reg_prediction": rf_reg_pred.tolist(),
            "logistic_prediction": log_pred.tolist()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Step 4: Optional root route
@app.route('/', methods=['GET'])
def home():
    return "✅ Flask server is running!"

# Step 5: Run app
if __name__ == "__main__":
    app.run(port=8000, debug=True)
