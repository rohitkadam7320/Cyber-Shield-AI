import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "database", "cybershield.db")
MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "model.pkl")
