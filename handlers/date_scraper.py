from aiogram import types, Dispatcher
from create_bot import dispatcher
from keyboards import bttns

from bs4 import BeautifulSoup
import requests

import logging
import datetime
import emoji


logging.basicConfig(filename="./logs/logs.txt", filemode='w', level=logging.INFO)

# ---------- /week ----------
# @dispatcher.message_handler(commands=['week'])
async def say_week(message: types.Message):
	# This command return an information from site of MIREA
	try:
		url = 'https://www.mirea.ru/'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')

		quotes = soup.find_all('div', class_='bonus_cart-title')
		data = ''

		for quote in quotes:
			data = quote.text

		await message.answer(text=emoji.emojize(":spiral_calendar:") + f'<b>Сегодня</b>: {data}', parse_mode='html', reply_markup=bttns)
		logging.info(f"Date was sent successfully, user={message.from_user}, time={datetime.datetime.now()}")
	except requests.exceptions.InvalidURL:
		await message.answer(text="Извини, я не смог получить данные с сайта МИРЭА")
		logging.info(f"Not found, user={message.from_user}, time={datetime.datetime.now()}")


def register_handlers_date_scraper(dp: Dispatcher):
	dp.register_message_handler(say_week, text=['📆Неделя', 'Неделя', 'week'])