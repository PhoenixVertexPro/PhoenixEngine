from flask import Flask, render_template, jsonify
from engine.core import engine_status
from engine.signals import generate_signal
from api.api_main import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify(engine_status())

@app.route("/signal")
def signal():
    return jsonify(generate_signal())

def start_dashboard():
    app.run(host="0.0.0.0", port=8000)
