def generate_signal():
    """
    تولید یک سیگنال نمونه برای PhoenixEngine.
    بعداً می‌توانیم این بخش را به موتور تحلیل واقعی وصل کنیم.
    """
    return {
        "pair": "BTC/USDT",
        "action": "BUY",
        "entry": 64200,
        "target": 65000,
        "stop": 63500
    }
