from flask import Blueprint, jsonify
from backend.database import get_connection

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/stats/<int:user_id>")
def stats(user_id):
    conn = get_connection()

    total = conn.execute(
        "SELECT COUNT(*) FROM scans WHERE user_id=?", (user_id,)
    ).fetchone()[0]

    threats = conn.execute(
        "SELECT COUNT(*) FROM scans WHERE user_id=? AND threat_level IN ('Suspicious','Malicious')",
        (user_id,)
    ).fetchone()[0]

    safe = conn.execute(
        "SELECT COUNT(*) FROM scans WHERE user_id=? AND threat_level='Safe'",
        (user_id,)
    ).fetchone()[0]

    recent = conn.execute(
        "SELECT * FROM scans WHERE user_id=? ORDER BY id DESC LIMIT 10",
        (user_id,)
    ).fetchall()

    conn.close()

    return jsonify(
        total_scans=total,
        threats=threats,
        safe=safe,
        recent_scans=[dict(x) for x in recent]
    )
