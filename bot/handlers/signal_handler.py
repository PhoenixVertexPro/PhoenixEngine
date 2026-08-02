from telegram import Update
from telegram.ext import ContextTypes
from services.signals import generate_signal

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sig = generate_signal()

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
