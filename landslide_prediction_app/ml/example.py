#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
dataset = pd.read_csv('../ml/landslide_dataset.csv')

# Features & target
X = dataset.drop(columns=['Label'])
y = dataset['Label']

# Split the data: 80% train, 20% test
X_train, X_test, Y_train, Y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
rf_model.fit(X_train, Y_train)

# Random Forest Regressor (for intensity)
rf_reg = RandomForestRegressor(n_estimators=150, random_state=42)
rf_reg.fit(X_train, Y_train)

# Logistic Regression with StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression(max_iter=1000, solver='lbfgs')
log_model.fit(X_train_scaled, Y_train)

# Save models and scaler
joblib.dump(rf_model, 'rf_classifier.pkl')
joblib.dump(rf_reg, 'rf_regressor.pkl')
joblib.dump(log_model, 'logistic_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ Models and scaler saved successfully")
