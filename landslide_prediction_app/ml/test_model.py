import pandas as pd
import joblib

# Load models
rf_model = joblib.load('rf_classifier.pkl')
rf_reg = joblib.load('rf_regressor.pkl')
log_model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load dataset
dataset = pd.read_csv('landslide_dataset.csv')
X = dataset.drop(columns=['Label'])

# Scale for logistic regression
X_scaled = scaler.transform(X)

# Make predictions
rf_pred = rf_model.predict(X)
rf_reg_pred = rf_reg.predict(X)
log_pred = log_model.predict(X_scaled)

print("Random Forest Classifier sample predictions:", rf_pred[:5])
print("Random Forest Regressor sample predictions:", rf_reg_pred[:5])
print("Logistic Regression sample predictions:", log_pred[:5])
