
from flask import Blueprint, jsonify
from engine.core import engine_status
from engine.signals import generate_signal

api = Blueprint("api", __name__)

@api.route("/engine")
def engine_info():
    return jsonify(engine_status())

@api.route("/signal")
def signal_info():
    return jsonify(generate_signal())
