# Insurance Charge Predictor 🏥

So basically this is a machine learning project where I'm trying to predict how much someone's insurance would cost based on stuff like their age, BMI, whether they smoke, etc. Built this while learning ML — it's a work in progress but it works!

## What does it actually do?

1. **Loads & cleans the data** — fixes messy values, handles missing rows, standardises text (like making all region names lowercase)
2. **Explores the data** — plots a scatter chart of age vs charges just to see what's going on
3. **Encodes the data** — converts text columns (sex, region, smoker) into numbers so the model can understand them
4. **Trains a Linear Regression model** — uses scikit-learn to predict insurance charges
5. **Evaluates accuracy** — checks MAE, MSE, and R² score to see how good the predictions are
6. **Predicts on new data** — runs the model on a validation dataset to get real predictions

## Dataset

- **Source:** [Keith Galli's Regression Example](https://github.com/KeithGalli/Regression-Example)
- **Features used:** age, sex, bmi, children, smoker, region
- **Target (what we're predicting):** insurance charges

## How to run it

**1. Clone the repo**
```bash
git clone https://github.com/PRB18/insurance_prediction.git
cd insurance_prediction
```

**2. Set up a virtual environment** (so packages don't mess up your system Python)
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Open the notebook**
```bash
jupyter notebook insurance.ipynb
```
Or just open it in VS Code and pick `.venv` as the kernel — then run all cells top to bottom.

## Files

| File | What it is |
|------|------------|
| `insurance.ipynb` | The main notebook — all the code lives here |
| `cleaned_insurance_data.csv` | The dataset after cleaning (auto-generated when you run the notebook) |
| `validation_dataset.csv` | New data the model predicts on (Step 6) |
| `requirements.txt` | All the Python packages needed |

## Tech used

- Python 🐍
- pandas (data cleaning)
- matplotlib (plotting)
- scikit-learn (the actual ML model)

