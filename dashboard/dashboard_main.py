from flask import Flask, render_template
from services.vip import VIP_USERS
from services.signals import generate_signal

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vip")
def vip_page():
    return render_template("vip.html", vip_users=VIP_USERS)

@app.route("/signals")
def signals_page():
    sig = generate_signal()
    return render_template("signals.html", signal=sig)

@app.route("/projects")
def projects_page():
    # بعداً از دیتابیس یا API تغذیه می‌شود
    projects = [
        {"name": "TON Ecosystem", "type": "Launchpad", "risk": "Medium"},
        {"name": "Solana AI Tokens", "type": "Trend", "risk": "High"},
    ]
    return render_template("projects.html", projects=projects)

@app.route("/referral")
def referral_page():
    referrals = [
        {"exchange": "BingX", "profit": "50%"},
        {"exchange": "Bybit", "profit": "40%"},
    ]
    return render_template("referral.html", referrals=referrals)

@app.route("/system")
def system_page():
    return render_template("system.html")

def start_dashboard():
    app.run(host="0.0.0.0", port=8000)
