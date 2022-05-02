from aiogram import types, Dispatcher
from create_bot import dispatcher
from handlers import keyboards
import logging


logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

cmd_strings = 'Use commands:\n/start\n/information\n/shedule\n/week\n/title'

# ---------- /title ----------
# @dispatcher.message_handler(commands=['title'])
async def giving_main_file(message: types.Message):
	try:
		await message.answer_document(document=('../files/title_page.docx', 'rb'), reply_markup=keyboards.bttns)
		logging.info("File was devivered successfully")
	except FileNotFoundError:
		await message.answer(text='I didn\'t find file, sorry(\n' + cmd_strings)
		logging.info("File Not Found")
	finally:
		await message.answer("What else?\n" + cmd_strings)


def register_handlers_giving_file(dp : Dispatcher):
	dp.register_message_handler(giving_main_file, commands=['title'])