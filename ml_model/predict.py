import joblib
from backend.config import MODEL_PATH

def predict(features):
    model = joblib.load(MODEL_PATH)
    result = model.predict([features])[0]
    confidence = model.predict_proba([features]).max()
    return result, round(confidence * 100, 2)
