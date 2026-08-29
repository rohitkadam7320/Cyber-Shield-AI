# CyberShield AI

Educational defensive cybersecurity project using Flask, SQLite and machine learning.

## Windows setup

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py

Open: http://127.0.0.1:5000

Optional:
python ml_model/train_model.py

Use only for authorized defensive/educational testing.
## 🔐 Password Strength Checker

CyberShield AI now includes a Password Strength Checker feature.

### Features
- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Provides password strength rating

### Password Levels
- Weak Password
- Medium Password
- Strong Password

### Technology Used
- Python
- Regular Expressions