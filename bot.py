# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import Bot, Dispatcher, executor, types
import logging
import psycopg2

import scraper
import xls_scraper
import keyboards

# Main object of our bot
bot = Bot(token='5224591766:AAEusyMiqE_lkFESzCS58w9bPCYyMHt8S3s')

# Dispatcher for shedule_KPK_bot
dispatcher = Dispatcher(bot)

# Logs will be ON
logging.basicConfig(filename="./logs/logs.txt", filemode='w', level=logging.INFO)


# need enter "/" before using a command
@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.answer(text='Hi, {0}, I\'m a shedule_KPK_bot Basic commands for me:\n/start\n/title\n/shedule\n/week'.format(message.from_user.first_name), reply_markup=keyboards.bttns)
		logging.info("Greeted")


@dispatcher.message_handler(commands='title')
async def giving_main_file(message: types.Message):
	try:
		await message.answer_document(document=open('./files/title page.docx', 'rb'), reply_markup=keyboards.bttns)
		logging.info("File was devivered successfully")
	except FileNotFoundError:
		await message.answer(text='I didn\'t find file, sorry(\nUse this commands:\n/start\n/title\n/shedule\n/week')
		logging.info("File Not Found")
	finally:
		await message.answer("What else?\n/start\n/title\n/shedule\n/week")


@dispatcher.message_handler(commands='shedule')
async def giving_shedule(message: types.Message):
	await message.answer(text=xls_scraper.result)
	logging.info("Shedule was sent successfully")


@dispatcher.message_handler(commands='week')
async def say_week(message: types.Message):
	await message.answer(text='Date: {0}'.format(scraper.data))
	logging.info("Date was sent successfully")


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False)