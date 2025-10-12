import express from "express";
import { predictLandslide } from "../controllers/predictController.js";

const router = express.Router();

router.post("/predict", predictLandslide);

export default router;
