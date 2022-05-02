from aiogram import types, Dispatcher
from create_bot import dispatcher
from keyboards import bttns
import logging


logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

strings = 'Попробуй:\n/start\n/information\n/shedule\n/week\n/title'

# ---------- /title ----------
# @dispatcher.message_handler(commands=['title'])
async def giving_main_file(message: types.Message):
	try:
		await message.answer_document(document=('../files/title_page.docx', 'rb'), reply_markup=bttns)
		logging.info("File was devivered successfully")
	except FileNotFoundError:
		await message.answer(text='Прости, я почему-то не нашел файл. Мой администратор вскоре исправит ситуацию)\n' + strings, reply_markup=bttns)
		logging.info("File Not Found")
	finally:
		await message.answer("Могу ли я помочь еще чем-то?\n" + strings)


def register_handlers_giving_file(dp : Dispatcher):
	dp.register_message_handler(giving_main_file, commands=['title'])