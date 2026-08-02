import os
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.start_handler import start
from services.vip import check_vip
from services.signals import generate_signal


async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if check_vip(user_id):
        await update.message.reply_text(
            "✅ شما عضو VIP PhoenixEngine هستید.\n"
            "به‌زودی امکانات بیشتری برای شما فعال می‌شود."
        )
    else:
        await update.message.reply_text(
            "❌ شما در لیست VIP نیستید.\n"
            "برای عضویت، با ادمین کانال تماس بگیرید."
        )


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


def start_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN در محیط تنظیم نشده است.")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("signal", signal))

    app.run_polling()
