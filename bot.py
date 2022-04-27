# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types

# Main object of our bot
bot = Bot(token='5224591766:AAEusyMiqE_lkFESzCS58w9bPCYyMHt8S3s')

# Dispatcher for shedule_KPK_bot
dispatcher = Dispatcher(bot)

# Logs will be ON
logging.basicConfig(level=logging.INFO)


@dispatcher.message_handler(commands='Hi')	# need "/" before command
async def greeting(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.reply("Hi, {0}, I am a shedule_KPK_bot".format(message.from_user.first_name))


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=True)