from telegram.ext import ApplicationBuilder, CommandHandler
from bot.handlers.start_handler import start
from services.vip import check_vip
from services.signals import generate_signal

async def start(update, context):
    await update.message.reply_text("PhoenixEngine فعال شد 🔥")

async def vip(update, context):
    user_id = update.message.from_user.id
    if check_vip(user_id):
        await update.message.reply_text("شما VIP هستید ✔")
    else:
        await update.message.reply_text("شما VIP نیستید ❌")

async def signal(update, context):
    sig = generate_signal()
    await update.message.reply_text(f"""
📈 سیگنال PhoenixEngine

Pair: {sig['pair']}
Action: {sig['action']}
Entry: {sig['entry']}
Target: {sig['target']}
Stop: {sig['stop']}
""")

def start_bot():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("signal", signal))

    app.run_polling()
