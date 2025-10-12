# Landslide Prediction System
A data-driven machine learning solution to predict landslide-prone regions using environmental, meteorological, and geological parameters, powered by **IBM Z / LinuxONE** for enterprise-grade scalability and reliability.


# Problem Statement
Landslides are severe natural disasters that cause widespread destruction, loss of life, and economic damage.

Our goal is to analyze multi-source environmental and geological data to **predict landslide risk** with high accuracy, enabling **early warnings** and **disaster mitigation**.


# Project Goal
Use **data-driven ML models** to analyze critical factors such as rainfall, elevation, vegetation, and soil conditions to **predict landslide-prone regions** with high accuracy.


# Target Audience & Benefits
* **Disaster Management Authorities**
    Use the model’s predictions to plan preventive measures, issue early warnings, and reduce potential damage from landslides.
* **Government & Local Bodies**
    Utilize predictions for policy making, infrastructure planning, and resource allocation in vulnerable regions.
* **Environmental & Geological Agencies**
   Apply the system for soil stability monitoring, environmental research, and terrain-based safety assessments.
* **Urban Planners & Civil Engineers**
   Use risk data to guide construction planning, slope stabilization, and safe zone design for buildings and roads.
* **Residents in Hilly or High-Rainfall Areas**
   Benefit from timely alerts, risk awareness insights, and evacuation readiness information for personal safety.

# Dataset Overview
The project uses **32 key attributes** from environmental, geological, and meteorological sources.

These datasets form the foundation for accurate prediction and pattern discovery.

## Key Feature Categories:
### Rainfall & Weather:
Rainfall_mm, Rainfall_3Day, Rainfall_7Day, Temperature_C, Humidity_percent
### Terrain & Topography:
Aspect, Elevation_m, NDVI_Index, Proximity_to_Water, Distance_to_Road_m
### Land Use & Vegetation:
Land_Use_Urban, Land_Use_Forest, Land_Use_Agriculture
### Seismic & Microseismic Activity:
Earthquake_Activity, Microseismic_Activity, Acoustic_Emission_dB
### Soil Properties:
Soil_pH, Clay_Content, Sand_Content, Silt_Content, Soil_Erosion_Rate,
Soil_Type_Gravel, Soil_Type_Sand, Soil_Type_Silt, Soil_Type_Clay,
Pore_Water_Pressure_kPa, Soil_Moisture_Content, Soil_Strain, Soil_Temperature_C, TDR_Reflection_Index
### Historical Data & Labels:
Historical_Landslide_Count, Label


# Workflow
## 1. EDA & Preprocessing
Data visualization (charts, heatmaps, missing value analysis)
Encoding categorical variables
Feature scaling using StandardScaler
Correlation and feature importance analysis
## 2. Modeling
Random Forest Classifier → Binary prediction (landslide / non-landslide)
Logistic Regression → Interpretable risk assessment
## 3. Evaluation
Metrics: Accuracy (92%), Precision, Recall, F1 (0.88), ROC-AUC (0.94)
Key Predictors: _Rainfall_7Day, Elevation_m, NDVI_Index, Soil_Moisture_Content_
## 4. Deployment
Real-time prediction via Flask API
Interactive dashboards using React frontend
Models & scalers stored using Joblib


# Deployment & Tech Stack
### Platform:
The project is deployed on IBM Z / LinuxONE, a high-performance, secure, and enterprise-grade platform. It provides parallel processing for large datasets, excellent scalability, and a trusted environment for training and serving machine learning models efficiently.
### Languages & Libraries:
The system is developed using Python with major libraries including Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, and Joblib.
These libraries handle data preprocessing, model training, visualization, and model persistence.
### Machine Learning Models:
The core predictive models used are the Random Forest Classifier (for binary landslide detection) and Logistic Regression (for interpretable risk assessment).
An optional Random Forest Regressor is included to predict landslide intensity or probability values.
### Frontend & Backend:
The project uses a Flask backend API for model inference and a React frontend for user interaction.
This enables real-time predictions and visualization of landslide risk on an interactive interface.
### Preprocessing:
Input features are standardized using StandardScaler from Scikit-learn to ensure consistent model performance and balanced feature influence during training and prediction.
### Versioning & Model Saving:
The trained models and preprocessing objects are serialized using Joblib, allowing reproducible predictions, version tracking, and seamless integration with the deployment pipeline.


# Supporting Data
The dataset contains 32 features across environmental, meteorological, and geospatial domains.
* Train-Test Split: 80–20 (Stratified to preserve class balance)
* Best Model: Random Forest Classifier → 92% Accuracy, 0.88 F1, 0.94 ROC-AUC
* Feature Importance Highlights: Rainfall_7Day, Elevation_m, NDVI_Index, Soil_Moisture_Content


# How It Leverages IBM Z
Our solution is deployed on IBM Z / LinuxONE, taking advantage of:
  * Parallel Processing: Faster ML training on large-scale geospatial data
  * Enterprise Security: Trusted environment for multi-user access and data protection
  * Scalability: Supports both real-time inference and batch retraining workflows
  * Reliability: 24/7 uptime and seamless data handling


# Model Development (Jupyter Notebook Training)
1. Data Preprocessing:
     * Handle missing values, normalize rainfall/elevation, encode land use types
     * Verify relationships with correlation matrices and outlier analysis
2. Feature Selection:
     * Selected top 8 impactful features for optimized inference
3. Model Training:
     * Random Forest Classifier for robust binary classification
     * Logistic Regression for interpretable decision boundaries
4. Evaluation:
     * Accuracy: 92%, F1: 0.88, ROC-AUC: 0.94
     * Cross-validation for model stability
5. Deployment:
     * Serialized models (.joblib) integrated with Flask + React frontend
     * Real-time inference supported on IBM LinuxONE
  

# Outcome
1. Accurate and interpretable landslide prediction model
2. Real-time, ready-for-deployment application
3. Scalable on enterprise infrastructure
4. Supports disaster prevention, urban safety, and environmental monitoring 

## Demo
![WhatsApp Image 2025-10-12 at 14 13 14_59cad0b1](https://github.com/user-attachments/assets/26f9acff-8846-48bd-a561-8df7c6cd78bf)

# Future Enhancements
* Integrate satellite imagery (CNN model) for image-based terrain risk detection
* Add real-time IoT sensor data (rainfall, soil moisture) for live updates
* Build interactive GIS dashboard with live alerts

# Team
**Team Name: NEXORA**
**Event:** IBM Z Datathon 2025
NEXORA is a team of six data enthusiasts passionate about applying machine learning and geospatial analytics to solve real-world environmental challenges. Our collective goal is to build scalable, intelligent, and reliable systems that contribute to early disaster prediction and prevention.

# Contributors
* Shaik Samreen – Lead ML Engineer & Data Science Expert
* Akshara C – Full Stack Developer (API Development & Integration)
* Swathi S – Full Stack Developer (API Development & Integration)
* Arshitha MS – Frontend & UI/UX Designer
* Akshaya S K – Documentation Lead & Data Curator
* Pavithra P – Documentation Lead & Feature Evaluator
