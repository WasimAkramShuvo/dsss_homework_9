from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from transformers import pipeline

# AI pipeline
ai_pipeline = pipeline("text-generation", model="gpt2")

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I'm an AI assistant. How can I help you today?")

# Process messages
async def process(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    ai_response = ai_pipeline(user_message, max_length=100, num_return_sequences=1)[0]["generated_text"]
    await update.message.reply_text(ai_response)

# Main function to run the bot
def main() -> None:
    API_TOKEN = "7482195005:AAHI96a8VnipIf_G-5FPZfCrvmCdUEp_5bw" 
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
