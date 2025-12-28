# Satellite Property Valuation 🏠📡

This project predicts **house prices** using structured property features.  
The pipeline follows a clean ML workflow:

**EDA → Preprocessing → Modeling → Prediction**


## 📁 Project Structure

satellite-property-valuation/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── train_processed.csv
│   └── test_processed.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_tabular.ipynb
│
├── src/
│   ├── data_fetcher.py
│   ├── models.py
│   └── predict.py
│
├── outputs/
│   ├── price_model.pkl
│   └── predictions.csv
│
└── README.md

---

## 📊 Dataset

The dataset contains structured housing information such as:
- bedrooms, bathrooms
- square footage (living, lot, basement)
- location (zipcode, latitude, longitude)
- construction details (year built, renovation)

Target variable:
- **price**

---

## 🔍 Exploratory Data Analysis (EDA)

Notebook: `01_eda.ipynb`

Performed:
- Missing value analysis
- Feature distributions
- Correlation analysis
- Target (`price`) behavior

---

## ⚙️ Preprocessing

Notebook: `02_preprocessing.ipynb`

Steps:
- Dropped unnecessary columns
- Handled missing values
- Feature scaling using `StandardScaler`
- Generated processed train and test datasets

Output:
- `train_processed.csv`
- `test_processed.csv`

---

## 🤖 Model Training

Notebook: `03_model_tabular.ipynb`

- Model used: **RandomForestRegressor**
- Evaluation metrics:
  - RMSE
  - R² score
- Trained model saved as:
  - `outputs/price_model.pkl`

---

## 🔮 Prediction

Script: `src/predict.py`

- Loads trained model
- Predicts prices on test data
- Saves results to:
  - `outputs/predictions.csv`

---

## ▶️ How to Run

```bash
python src/data_fetcher.py
python src/models.py
python src/predict.py
