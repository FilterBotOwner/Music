import asyncio
from bot import Bot  # Ensure you have a correct import

bot = Bot()

async def main():
    await bot.run()  # Ensure 'run()' is an async function

asyncio.run(main())
