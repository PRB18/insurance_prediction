# Model Notes

## Algorithm: Linear Regression

Linear Regression assumes a linear relationship between input features and the target variable (insurance charges).

### Why Linear Regression?
- Simple and interpretable
- Fast to train
- Good baseline before trying complex models

### Feature Importance (approximate)
Based on coefficient magnitudes after encoding:

| Feature | Impact |
|---------|--------|
| smoker  | Very High ↑ |
| age     | High ↑ |
| bmi     | Moderate ↑ |
| children | Low ↑ |
| sex     | Minimal |
| region  | Minimal |

### Known Limitations
- Linear models may underfit if the true relationship is non-linear
- BMI and age interactions with smoker status are not captured well
- Outliers in charges (very high-cost patients) can skew the model

### Next Steps
- Try **Ridge / Lasso** regression to penalise large coefficients
- Try **Random Forest Regressor** to capture non-linear relationships
- Apply **log transformation** to the target variable to reduce skew
