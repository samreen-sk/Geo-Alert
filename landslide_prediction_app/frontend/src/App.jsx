import React, { useState } from "react";
import "./App.css";

const App = () => {
  // 🌧️ Only key input fields from the user, initialized empty
  const [formValues, setFormValues] = useState({
    Rainfall_7Day: "",
    Aspect: "",
    Elevation_m: "",
    Soil_Moisture_Content: "",
    Soil_Erosion_Rate: "",
    NDVI_Index: "",
    Soil_Type_Clay: "",
    Historical_Landslide_Count: "",
  });

  // ⚙️ State for prediction result
  const [carbonRisk, setCarbonRisk] = useState("Predicted Landslide Risk: -");

  // 🧮 Handle input change
  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormValues((prevValues) => ({
      ...prevValues,
      [id]: value
    }));
  };

  // 🔹 Map regressor output to Low/Medium/High
  const getRiskLevel = (value) => {
    if (value >= 0.7) return "High";
    if (value >= 0.4) return "Medium";
    return "Low";
  };

  // 🚀 Handle prediction
  const handlePredict = async () => {
    try {
      // 📝 Create full feature object with defaults for remaining features
      const fullFeatures = {
        Rainfall_mm: "100",
        Rainfall_3Day: "50",
        Rainfall_7Day: formValues.Rainfall_7Day || "120",
        Aspect: formValues.Aspect || "180",
        Elevation_m: formValues.Elevation_m || "450",
        NDVI_Index: formValues.NDVI_Index || "0.65",
        Land_Use_Urban: "0",
        Land_Use_Forest: "1",
        Land_Use_Agriculture: "0",
        Earthquake_Activity: "0",
        Proximity_to_Water: "200",
        Distance_to_Road_m: "50",
        Temperature_C: "25",
        Humidity_percent: "70",
        Soil_pH: "6.5",
        Clay_Content: "20",
        Sand_Content: "40",
        Silt_Content: "40",
        Soil_Erosion_Rate: formValues.Soil_Erosion_Rate || "0.3",
        Historical_Landslide_Count: formValues.Historical_Landslide_Count || "0",
        Soil_Type_Gravel: "0",
        Soil_Type_Sand: "0",
        Soil_Type_Silt: "0",
        Soil_Type_Clay: formValues.Soil_Type_Clay || "0",
        Pore_Water_Pressure_kPa: "15",
        Soil_Moisture_Content: formValues.Soil_Moisture_Content || "30",
        Microseismic_Activity: "0",
        Acoustic_Emission_dB: "35",
        Soil_Strain: "0.02",
        Soil_Temperature_C: "22",
        TDR_Reflection_Index: "0.01"
      };

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(fullFeatures)
      });

      const result = await response.json();

      if (response.ok) {
        const regValue = result.rf_reg_prediction[0]; // e.g., 0.18
        const level = getRiskLevel(regValue);
        setCarbonRisk(
          `Estimated Carbon Risk: ${(regValue * 100).toFixed(0)}% (${level})`
        );
      } else {
        alert(`Prediction failed: ${result.error || "Server error"}`);
      }
    } catch (error) {
      alert("Could not connect to the ML backend. Is Flask running on port 8000?");
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <div className="header-left-group">
          <img src="/ibm_logo.jpg" alt="IBM Logo" className="ibm-logo" />
          <img src="/linuxone-logo.jpg" alt="Linux Logo" className="linuxone-logo" />
        </div>
        <div className="header-center-group">
          <div className="ibm-datathon-text">IBM DATATHON 2025</div>
          <div className="landslide-prediction-title">Landslide Prediction System</div>
          <div className="subtitle">Estimate landslide risk in coastal and marine ecosystems</div>
        </div>
        <div className="header-right-group">
          <div className="team-info">Team NEXORA</div>
          <div className="team-name">SAV003</div>
        </div>
      </header>

      <main className="main-content">
        <div className="card">
          <h2 className="card-title">Enter Key Site Parameters</h2>
          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="Rainfall_7Day">Rainfall_7Day (mm)</label>
              <input
                type="text"
                id="Rainfall_7Day"
                value={formValues.Rainfall_7Day}
                onChange={handleChange}
                placeholder="e.g., 120"
              />
            </div>
            <div className="form-group">
              <label htmlFor="Aspect">Aspect (degrees)</label>
              <input
                type="text"
                id="Aspect"
                value={formValues.Aspect}
                onChange={handleChange}
                placeholder="e.g., 180"
              />
            </div>
            <div className="form-group">
              <label htmlFor="Elevation_m">Elevation (m)</label>
              <input
                type="text"
                id="Elevation_m"
                value={formValues.Elevation_m}
                onChange={handleChange}
                placeholder="e.g., 450"
              />
            </div>
            <div className="form-group">
              <label htmlFor="Soil_Moisture_Content">Soil Moisture Content (%)</label>
              <input
                type="text"
                id="Soil_Moisture_Content"
                value={formValues.Soil_Moisture_Content}
                onChange={handleChange}
                placeholder="e.g., 30"
              />
            </div>
            <div className="form-group">
              <label htmlFor="Soil_Erosion_Rate">Soil Erosion Rate</label>
              <input
                type="text"
                id="Soil_Erosion_Rate"
                value={formValues.Soil_Erosion_Rate}
                onChange={handleChange}
                placeholder="e.g., 0.3"
              />
            </div>
            <div className="form-group">
              <label htmlFor="NDVI_Index">NDVI Index</label>
              <input
                type="text"
                id="NDVI_Index"
                value={formValues.NDVI_Index}
                onChange={handleChange}
                placeholder="e.g., 0.65"
              />
            </div>
            <div className="form-group">
              <label htmlFor="Soil_Type_Clay">Soil Type Clay (0/1)</label>
              <input
                type="text"
                id="Soil_Type_Clay"
                value={formValues.Soil_Type_Clay}
                onChange={handleChange}
                placeholder="0 or 1"
              />
            </div>
            <div className="form-group">
              <label htmlFor="Historical_Landslide_Count">Historical Landslide Count</label>
              <input
                type="text"
                id="Historical_Landslide_Count"
                value={formValues.Historical_Landslide_Count}
                onChange={handleChange}
                placeholder="e.g., 0"
              />
            </div>
          </div>

          <button className="predict-button" onClick={handlePredict}>
            PREDICT LANDSLIDE RISK
          </button>
        </div>

        {/* 📊 Prediction Result */}
        <div className="carbon-risk-section">
          <h3>{carbonRisk}</h3>
        </div>
      </main>
    </div>
  );
};

export default App;
