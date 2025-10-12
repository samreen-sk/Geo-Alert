import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import predictRoutes from "./routes/predictRoutes.js";

dotenv.config();
const app = express();

app.use(cors());
app.use(express.json());

// Routes
app.use("/api", predictRoutes);

// Default Route
app.get("/", (req, res) => {
  res.send("✅ Backend is running successfully!");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Server started on port ${PORT}`));
