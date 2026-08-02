from flask import Flask, jsonify
from services.signals import generate_signal
from services.vip import check_vip

app = Flask(__name__)


@app.route("/api/signal")
def api_signal():
    sig = generate_signal()
    return jsonify(sig)


@app.route("/api/vip/<int:user_id>")
def api_vip(user_id: int):
    return jsonify({"user_id": user_id, "is_vip": check_vip(user_id)})


@app.route("/api/projects")
def api_projects():
    projects = [
        {"name": "TON Ecosystem", "type": "Launchpad", "risk": "Medium"},
        {"name": "Solana AI Tokens", "type": "Trend", "risk": "High"},
    ]
    return jsonify(projects)


@app.route("/api/referral")
def api_referral():
    referrals = [
        {"exchange": "BingX", "profit": "50%"},
        {"exchange": "Bybit", "profit": "40%"},
    ]
    return jsonify(referrals)


@app.route("/api/system")
def api_system():
    return jsonify({
        "bot": "online",
        "dashboard": "online",
        "services": "connected",
        "engine": "ready"
    })


def start_api():
    app.run(host="0.0.0.0", port=9000)
