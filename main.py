import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import BOT_TOKEN  # This imports your bot token from config.py

def start(update: Update, context: CallbackContext):
    """Responds to the /start command."""
    update.message.reply_text("Hello! I'm alive and ready to play music.")

def main():
    print("Initializing bot...")

    # Initialize the Updater and Dispatcher using your bot token
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add a command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    print("Starting bot polling...")
    updater.start_polling()

    print("Bot is running. Press Ctrl+C to stop.")

    # This call blocks until you press Ctrl+C, keeping the bot running
    updater.idle()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
