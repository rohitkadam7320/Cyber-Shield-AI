from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.database import init_db
from backend.routes.auth import auth
from backend.routes.scanner import scanner
from backend.routes.dashboard import dashboard
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__)
CORS(app)
init_db()

app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(scanner, url_prefix="/api/scanner")
app.register_blueprint(dashboard, url_prefix="/api/dashboard")

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:path>")
def frontend(path):
    return send_from_directory(FRONTEND_DIR, path)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
