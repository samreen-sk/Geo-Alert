# train_models.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error
import joblib

def main():
    print("✅ Loading dataset...")
    dataset = pd.read_csv('landslide_dataset.csv')

    # Features and target
    X = dataset.drop(columns=['Label'])
    y = dataset['Label']

    # Split data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # -------- Random Forest Classifier --------
    print("✅ Training Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
    rf_model.fit(X_train, Y_train)
    Y_pred = rf_model.predict(X_test)
    print("Random Forest Classifier Accuracy:", accuracy_score(Y_test, Y_pred))

    # -------- Random Forest Regressor --------
    print("✅ Training Random Forest Regressor...")
    rf_reg = RandomForestRegressor(n_estimators=150, random_state=42)
    rf_reg.fit(X_train, Y_train)
    Y_pred_reg = rf_reg.predict(X_test)
    mse = mean_squared_error(Y_test, Y_pred_reg)
    rmse = np.sqrt(mse)
    print("Random Forest Regressor RMSE:", rmse)

    # -------- Logistic Regression --------
    print("✅ Training Logistic Regression...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    log_model = LogisticRegression(max_iter=1000, solver='lbfgs')
    log_model.fit(X_train_scaled, Y_train)
    y_pred_log = log_model.predict(X_test_scaled)
    print("Logistic Regression Accuracy:", accuracy_score(Y_test, y_pred_log))

    # -------- Save models --------
    print("✅ Saving models...")
    joblib.dump(rf_model, 'rf_classifier.pkl')
    joblib.dump(rf_reg, 'rf_regressor.pkl')
    joblib.dump(log_model, 'logistic_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("🎉 All models and scaler saved successfully!")

    # Optional: return models if needed elsewhere
    return rf_model, rf_reg, log_model, scaler

if __name__ == "__main__":
    main()
