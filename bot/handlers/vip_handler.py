from telegram import Update
from telegram.ext import ContextTypes
from services.vip import check_vip

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
