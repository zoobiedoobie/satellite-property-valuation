import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "outputs", "price_model.pkl")
DATA_PATH  = os.path.join(BASE_DIR, "data", "test_processed.csv")
OUT_PATH   = os.path.join(BASE_DIR, "outputs", "predictions.csv")

model = joblib.load(MODEL_PATH)

test_df = pd.read_csv(DATA_PATH)
preds = model.predict(test_df)

pd.DataFrame({"predicted_price": preds}).to_csv(OUT_PATH, index=False)

print("Predictions saved successfully!")
