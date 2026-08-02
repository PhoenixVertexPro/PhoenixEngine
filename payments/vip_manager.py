# payments/vip_manager.py

import json
import time

DB_PATH = "payments/vip_database.json"

def load_db():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def add_vip(user_id, plan):
    db = load_db()
    db[str(user_id)] = {
        "plan": plan,
        "timestamp": time.time()
    }
    save_db(db)
    return True

def is_vip(user_id):
    db = load_db()
    return str(user_id) in db
