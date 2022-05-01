# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import states
import scraper
import xls_scraper
import keyboards
import information

# main object of our bot
bot = Bot(token='5224591766:AAEusyMiqE_lkFESzCS58w9bPCYyMHt8S3s')

# dispatcher for shedule_KPK_bot
dispatcher = Dispatcher(bot, storage=MemoryStorage())

# logs will be ON
logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

# for fast change a list of commands
cmd_strings = 'Use commands:\n/start\n/information\n/shedule\n/week\n/title'

# need enter "/" before using a command

# ---------- /start ----------
@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.answer(text=f'Hi, {message.from_user.first_name}, I\'m a shedule_KPK_bot.' + cmd_strings, reply_markup=keyboards.bttns)
		logging.info("Greeted successfully")


# ---------- /information ----------
@dispatcher.message_handler(commands='information')
async def giving_information(message: types.Message):
	await message.answer(text=information.inf_college)
	logging.info("Information was sent successfully")


# ---------- /title ----------
@dispatcher.message_handler(commands='title')
async def giving_main_file(message: types.Message):
	try:
		await message.answer_document(document=('./files/title_page.docx', 'rb'), reply_markup=keyboards.bttns)
		logging.info("File was devivered successfully")
	except FileNotFoundError:
		await message.answer(text='I didn\'t find file, sorry(\n' + cmd_strings)
		logging.info("File Not Found")
	finally:
		await message.answer("What else?\n" + cmd_strings)


# ---------- /shedule ----------
@dispatcher.message_handler(Command('shedule'), state=None)
async def say_group(message: types.Message, state: FSMContext):
	await message.answer(text="Enter Your Group: ")
	await states.Group.student_group.set()


@dispatcher.message_handler(state=states.Group.student_group)
async def giving_shedule(message: types.Message, state: FSMContext):
	#data = dispatcher.current_state(chat=message.chat.id, user=message.from_user.id)
	data2 = message.text
	print(data2)
	#print(data)
	await state.update_data(answer=data2)

	if data2:
		try:
			await message.answer(text=xls_scraper.result)
			logging.info("Shedule was sent successfully")
		except FileNotFoundError:
			await message.answer(text='I didn\'t find file, sorry(\n' + cmd_strings)
			logging.info("File Not Found")
			
	await state.reset_state(with_data=False)
	await state.finish()

# ---------- /week ----------
@dispatcher.message_handler(commands='week')
async def say_week(message: types.Message):
	await message.answer(text=f'Date: {scraper.data}')
	logging.info("Date was sent successfully")


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False)