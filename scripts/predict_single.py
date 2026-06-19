"""
predict_single.py — Predict insurance charges for a single person

Trains the model on the full cleaned dataset, then predicts for
a manually defined individual.

Usage:
    python scripts/predict_single.py
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# ── Load and prepare training data ──────────────────────────────────
df = pd.read_csv("cleaned_insurance_data.csv")

le_sex    = LabelEncoder().fit(["female", "male"])
le_smoker = LabelEncoder().fit(["no", "yes"])
le_region = LabelEncoder().fit(["northeast", "northwest", "southeast", "southwest"])

df["sex"]    = le_sex.transform(df["sex"])
df["smoker"] = le_smoker.transform(df["smoker"])
df["region"] = le_region.transform(df["region"])

X = df.drop(columns=["charges"])
y = df["charges"]

model = LinearRegression()
model.fit(X, y)

# ── Define your person here ──────────────────────────────────────────
person = {
    "age":      28,
    "sex":      "male",    # male / female
    "bmi":      24.5,
    "children": 0,
    "smoker":   "no",      # yes / no
    "region":   "southwest"  # northeast / northwest / southeast / southwest
}

# ── Encode ───────────────────────────────────────────────────────────
person_encoded = {
    "age":      person["age"],
    "sex":      le_sex.transform([person["sex"]])[0],
    "bmi":      person["bmi"],
    "children": person["children"],
    "smoker":   le_smoker.transform([person["smoker"]])[0],
    "region":   le_region.transform([person["region"]])[0],
}

person_df = pd.DataFrame([person_encoded])

# ── Predict ──────────────────────────────────────────────────────────
prediction = model.predict(person_df)[0]

print("\n── Input Profile ──────────────────────────")
for k, v in person.items():
    print(f"  {k:<10}: {v}")
print("───────────────────────────────────────────")
print(f"  Predicted Annual Charges: ${prediction:,.2f}")

# Simple risk interpretation
if prediction < 8000:
    risk = "Low 🟢"
elif prediction < 16000:
    risk = "Moderate 🟡"
else:
    risk = "High 🔴"

print(f"  Risk Level              : {risk}")
print("───────────────────────────────────────────\n")
