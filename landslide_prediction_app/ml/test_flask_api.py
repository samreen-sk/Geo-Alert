import requests

# Example values for all features (replace with real numbers)
data = {
    "Rainfall_mm": 100,
    "Rainfall_3Day": 50,
    "Rainfall_7Day": 120,
    "Aspect": 180,
    "Elevation_m": 450,
    "NDVI_Index": 0.65,
    "Land_Use_Urban": 0,
    "Land_Use_Forest": 1,
    "Land_Use_Agriculture": 0,
    "Earthquake_Activity": 0,
    "Proximity_to_Water": 300,
    "Distance_to_Road_m": 150,
    "Temperature_C": 25,
    "Humidity_percent": 80,
    "Soil_pH": 6.5,
    "Clay_Content": 20,
    "Sand_Content": 40,
    "Silt_Content": 40,
    "Soil_Erosion_Rate": 2,
    "Historical_Landslide_Count": 1,
    "Soil_Type_Gravel": 0,
    "Soil_Type_Sand": 1,
    "Soil_Type_Silt": 0,
    "Soil_Type_Clay": 0,
    "Pore_Water_Pressure_kPa": 15,
    "Soil_Moisture_Content": 0.25,
    "Microseismic_Activity": 0,
    "Acoustic_Emission_dB": 30,
    "Soil_Strain": 0.01,
    "Soil_Temperature_C": 22,
    "TDR_Reflection_Index": 0.5
}

response = requests.post("http://127.0.0.1:8000/predict", json=data)

print("Response from Flask API:")
print(response.json())
