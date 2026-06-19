# Changelog

All notable changes to this project will be documented here.

## [Unreleased]
- Exploring Random Forest and XGBoost models for improved accuracy
- Plan to add cross-validation for more robust evaluation

## [0.4.0] - 2026-06-19
### Added
- `docs/model_notes.md` — feature importance, limitations, next steps, evaluation methodology
- `docs/data_dictionary.md` — full column descriptions and encoding map
- `scripts/evaluate.py` — standalone script to retrain and print model metrics
- `scripts/predict_single.py` — predict charges for a custom individual
- `.gitignore` for Python, Jupyter, and virtual environments
- MIT `LICENSE`

## [0.3.0] - 2026-06-17
### Added
- Linear Regression model training and evaluation
- Validation dataset predictions
- Model metrics: MAE, MSE, R² score

## [0.2.0] - 2026-06-16
### Added
- Label encoding for categorical columns (sex, smoker, region)
- Feature-target split for model training

## [0.1.0] - 2026-06-15
### Added
- Data loading and cleaning pipeline
- Exploratory scatter plot (age vs charges)
- Exported `cleaned_insurance_data.csv`
