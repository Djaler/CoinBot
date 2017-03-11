import os

from bot import Bot


token = os.environ.get("TOKEN")

bot = Bot(token)
bot.run()
