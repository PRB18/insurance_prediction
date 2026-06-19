# Data Dictionary

## Dataset: Insurance Charges

Source: [Keith Galli's Regression Example](https://github.com/KeithGalli/Regression-Example)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `age` | Integer | Age of the primary beneficiary | 25 |
| `sex` | String → Encoded | Biological sex of the policyholder | `male`, `female` → 0, 1 |
| `bmi` | Float | Body Mass Index (kg/m²) | 28.5 |
| `children` | Integer | Number of dependents covered | 2 |
| `smoker` | String → Encoded | Whether the person smokes | `yes`, `no` → 1, 0 |
| `region` | String → Encoded | US geographic region | `southwest`, `northeast`, etc. |
| `charges` | Float | Annual insurance cost (USD) — **target variable** | 14,045.00 |

## Encoding Map

| Column | Original | Encoded |
|--------|----------|---------|
| sex | male | 0 |
| sex | female | 1 |
| smoker | no | 0 |
| smoker | yes | 1 |
| region | northeast | 0 |
| region | northwest | 1 |
| region | southeast | 2 |
| region | southwest | 3 |

## Notes
- `bmi` values were standardised to 2 decimal places during cleaning
- Rows with missing `charges` were dropped
- Text columns were lowercased before encoding
