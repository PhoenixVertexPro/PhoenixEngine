import requests
from telegram import Update
from telegram.ext import ContextTypes

API_URL = "https://YOUR-RAILWAY-API-URL/api/signal"

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        sig = requests.get(API_URL).json()

        text = f"""
📡 PhoenixEngine Signal

🔹 Pair: {sig['pair']}
🔹 Action: {sig['action']}
🔹 Entry: {sig['entry']}
🔹 Target: {sig['target']}
🔹 Stop: {sig['stop']}

⚠️ مدیریت سرمایه فراموش نشود.
"""
        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text("❌ خطا در دریافت سیگنال از API")
        print("Signal API Error:", e)
