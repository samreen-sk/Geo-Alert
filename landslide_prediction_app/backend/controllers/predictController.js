import axios from "axios";

export const predictLandslide = async (req, res) => {
  try {
    // Forward the frontend data to the Python Flask ML API
const response = await axios.post("http://127.0.0.1:8000/predict", req.body);

    res.json({
      estimated_risk: response.data.estimated_risk,
    });
  } catch (error) {
    console.error("Prediction Error:", error.message);
    res.status(500).json({
      error: "Failed to connect to ML model or compute prediction.",
    });
  }
};
