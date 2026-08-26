from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database import get_connection

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    if not all(data.get(k) for k in ("name", "email", "password")):
        return jsonify(success=False, message="All fields are required"), 400
    try:
        conn = get_connection()
        conn.execute(
            "INSERT INTO users (name,email,password) VALUES (?,?,?)",
            (data["name"], data["email"], generate_password_hash(data["password"]))
        )
        conn.commit()
        conn.close()
        return jsonify(success=True, message="Registration successful")
    except Exception:
        return jsonify(success=False, message="Email already exists"), 409

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE email=?", (data.get("email"),)
    ).fetchone()
    conn.close()

    if user and check_password_hash(user["password"], data.get("password", "")):
        return jsonify(
            success=True,
            message="Login successful",
            user={"id": user["id"], "name": user["name"], "email": user["email"]}
        )

    return jsonify(success=False, message="Invalid email or password"), 401
