from flask import Blueprint, request, jsonify
from backend.database import get_connection
from backend.services.url_scanner import basic_url_analysis

scanner = Blueprint("scanner", __name__)

@scanner.route("/scan-url", methods=["POST"])
def scan_url():
    data = request.get_json() or {}
    url = data.get("url")

    if not url:
        return jsonify(success=False, message="URL is required"), 400

    valid, score, level = basic_url_analysis(url)

    if not valid:
        return jsonify(success=False, message="Invalid URL"), 400

    conn = get_connection()
    conn.execute(
        "INSERT INTO scans (user_id,input_value,result,risk_score,threat_level) VALUES (?,?,?,?,?)",
        (data.get("user_id"), url, level, score, level)
    )
    conn.commit()
    conn.close()

    return jsonify(success=True, result=level, risk_score=score)
