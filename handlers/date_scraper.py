from aiogram import types, Dispatcher
from create_bot import dispatcher
from keyboards import bttns

from bs4 import BeautifulSoup
import requests
import logging


logging.basicConfig(filename="./logs/logs.txt", filemode='w', level=logging.INFO)

# ---------- /week ----------
# @dispatcher.message_handler(commands=['week'])
async def say_week(message: types.Message):
	url = 'https://www.mirea.ru/'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	quotes = soup.find_all('div', class_='bonus_cart-title')
	data = ''

	for quote in quotes:
		data = quote.text

	await message.answer(text=f'Сегодня: {data}', reply_markup=bttns)
	logging.info("Date was sent successfully")


def register_handlers_date_scraper(dp: Dispatcher):
	dp.register_message_handler(say_week, commands=['week'])