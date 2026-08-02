from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 خوش آمدید به PhoenixEngine\n\n"
        "دستورات:\n"
        "/signal — دریافت سیگنال عمومی\n"
        "/vip — بررسی وضعیت VIP\n\n"
        "به‌زودی امکانات بیشتری فعال می‌شود…"
    )
