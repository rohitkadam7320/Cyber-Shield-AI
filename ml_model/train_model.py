import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(os.path.join(BASE, "dataset", "phishing_dataset.csv"))
X = df.drop("label", axis=1)
y = df["label"]

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(Xtr, ytr)

print("Accuracy:", accuracy_score(yte, model.predict(Xte)))

joblib.dump(model, os.path.join(BASE, "ml_model", "model.pkl"))
print("Model saved.")
