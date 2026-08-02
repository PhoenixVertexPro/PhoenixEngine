# engine/signals.py

def generate_auto_signal():
    """
    موتور تولید سیگنال خودکار
    در آینده می‌تواند به APIهای واقعی وصل شود
    """
    return {
        "pair": "ETH/USDT",
        "action": "BUY",
        "entry": 3120,
        "target": 3200,
        "stop": 3050,
    }
