from aiogram import types, Dispatcher
from create_bot import dispatcher
from keyboards import bttns
import logging
import datetime

logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)


# ---------- /main_page ----------
# @dispatcher.message_handler(commands=['main_page'])
async def giving_main_file(message: types.Message):
	try:
		doc = open('./files/title_page.docx', 'rb')
		await message.reply_document(doc, reply_markup=bttns)
		logging.info(f"File was devivered successfully, user={message.from_user}, time={datetime.datetime.now()}")
	except FileNotFoundError:
		await message.answer(text='Прости, я почему-то не нашел файл. Мой администратор вскоре исправит ситуацию)\n', reply_markup=bttns)
		logging.info(f"File Not Found, user={message.from_user}, time={datetime.datetime.now()}")


def register_handlers_giving_file(dp : Dispatcher):
	dp.register_message_handler(giving_main_file, text=['📃Титульник', 'Титульник', 'title'])
