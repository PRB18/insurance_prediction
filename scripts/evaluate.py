"""
evaluate.py — Quick model evaluation helper

Run this script to retrain the linear regression model and print metrics.
Usage:
    python scripts/evaluate.py
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load cleaned data
df = pd.read_csv("cleaned_insurance_data.csv")

# Encode categorical columns
le = LabelEncoder()
for col in ["sex", "smoker", "region"]:
    df[col] = le.fit_transform(df[col])

# Split features and target
X = df.drop(columns=["charges"])
y = df["charges"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("=" * 40)
print("  Insurance Prediction — Model Metrics")
print("=" * 40)
print(f"  R² Score : {r2_score(y_test, y_pred):.4f}")
print(f"  MAE      : ${mean_absolute_error(y_test, y_pred):,.2f}")
print(f"  MSE      : {mean_squared_error(y_test, y_pred):,.2f}")
print("=" * 40)

# Feature coefficients
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values("Coefficient", ascending=False)

print("\nFeature Coefficients:")
print(coef_df.to_string(index=False))
