# Insurance Prediction

A machine learning project to analyze and predict insurance charges based on patient data.

## Dataset
- Source: [Keith Galli's Regression Example](https://github.com/KeithGalli/Regression-Example)
- Features: age, sex, bmi, children, smoker, region
- Target: insurance charges

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/PRB18/insurance_prediction.git
cd insurance_prediction
```

**2. Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Open the notebook**
```bash
jupyter notebook insurance.ipynb
```
Or open in VS Code and select `.venv` as the kernel.

## Files
| File | Description |
|------|-------------|
| `insurance.ipynb` | Main notebook with data cleaning and analysis |
| `cleaned_insurance_data.csv` | Cleaned dataset exported after preprocessing |
| `requirements.txt` | All Python dependencies |
