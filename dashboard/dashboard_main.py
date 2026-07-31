from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Phoenix Dashboard Online 🔥"

@app.route("/status")
def status():
    data = {
        "engine": "online",
        "bot": "online",
        "version": "v1.0.0"
    }
    return jsonify(data)

def start_dashboard():
    app.run(host="0.0.0.0", port=8000)
