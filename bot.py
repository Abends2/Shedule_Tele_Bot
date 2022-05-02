# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from openpyxl import load_workbook
import logging
import requests
from bs4 import BeautifulSoup

import keyboards

# main object of our bot
bot = Bot(token='5224591766:AAEusyMiqE_lkFESzCS58w9bPCYyMHt8S3s')

# dispatcher for shedule_KPK_bot
dispatcher = Dispatcher(bot, storage=MemoryStorage())

# logs will be ON
logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

# need for State
class Group(StatesGroup):
	student_group = State()

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
	inf_college = """
	Информация о колледже:
	- Полное наименование Колледжа: Колледж программирования и кибербезопасности
	- Сокращенное наименование: КПК
	- Наименование Колледжа на английском языке: Сollege of programming and cyber security
	- Адрес местонахождения: Москва, 1-Щипковский переулок, д. 23. 
	"""

	inf_profession = """
	Специальности:
	1) 09.02.01 Компьютерные системы и комплексы
	2) 09.02.03 Программирование в компьютерных системах
	3) 09.02.06 Сетевое и системное администрирование
	4) 09.02.07 Информационные системы и программирование
	5) 10.02.04 Обеспечение информационной безопасности телекоммуникационных систем
	6) 10.02.05 Обеспечение информационной безопасности автоматизированных систем
	7) 11.02.15 Инфокоммуникационные сети и системы связи
	8) 12.02.05 Оптические и оптико-электронные приборы и системы
	9) 12.02.09 Производство и эксплуатация оптических и оптикоэлектронных приборов и систем
	"""

	inf_university = """
	Информация о ВУЗ'е:
	- Полное наименование образовательной организации: Федеральное государственное бюджетное образовательное учреждение высшего образования "МИРЭА - Российский технологический университет"
	- Сокращенное наименование образовательной организации: РТУ МИРЭА
	"""

	inf_time = """
	Время проведения занятий:
	1 пара – 8:45-10:15
	2 пара – 10:25-11:55
	3 пара – 12:30-14:00
	4 пара – 14:35-16:05
	5 пара – 16:15-17:45
	"""
	await message.answer(text=inf_college)
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
@dispatcher.message_handler(commands='shedule', state=None)
async def say_group(message: types.Message, state: FSMContext):
	await message.answer(text="Enter Your Group: ")
	await Group.student_group.set()


@dispatcher.message_handler(state=Group.student_group)
async def giving_shedule(message: types.Message, state: FSMContext):
	data = message.text
	await state.update_data(answer=data)

	book = load_workbook(filename="../files/shedule.xlsx")
	sheet = book["Shedule"]

	groups = {'ИБ-21' : 'A',
			'ИБ-22': 'B',
			'ИБ-23': 'C'}

	result = ''

	if data in groups:
		for i in range(1, 32):
			cell = sheet[groups[data] + str(i)].value
			if ";" in cell:
				cell = cell[0:cell.find(";") + 1] + '\n' + '   ' + cell[cell.find(";") + 2:]
			result += cell + '\n'

	if data:
		try:
			await message.answer(text=result)
			logging.info("Shedule was sent successfully")
		except FileNotFoundError:
			await message.answer(text='I didn\'t find file, sorry(\n' + cmd_strings)
			logging.info("File Not Found")
	else:
		print("Группа не найдена")
			
	await state.reset_state(with_data=False)
	await state.finish()

# ---------- /week ----------
@dispatcher.message_handler(commands='week')
async def say_week(message: types.Message):
	url = 'https://www.mirea.ru/'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	quotes = soup.find_all('div', class_='bonus_cart-title')
	data = ''

	for quote in quotes:
		data = quote.text

	await message.answer(text=f'Date: {data}')
	logging.info("Date was sent successfully")


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False)