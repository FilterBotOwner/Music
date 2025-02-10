import time
from bot import Bot  # Ensure this file exists

print("Bot is starting...")

bot = Bot()  # Initialize the bot
bot.run()    # Start the bot

print("Bot is running...")

# Keep the bot running to prevent Koyeb from stopping it
while True:
    time.sleep(10)
