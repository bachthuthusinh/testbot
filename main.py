from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8690279748:AAHvEIDgH-q7br_vkirgyxuoGaBjX1VgbR4"
LOG_CHANNEL_ID = -1003884773685  # ID channel log

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.forward_message(
            chat_id=LOG_CHANNEL_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, log_message))
app.run_polling()