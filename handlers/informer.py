from aiogram import types, Dispatcher
from create_bot import dispatcher
from keyboards import bttns
import logging
import datetime

logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)


# ---------- /information ----------
# @dispatcher.message_handler(commands=['information'])
async def giving_information(message: types.Message):
	inf_general = """
	<b>Информация о колледже</b>:
	- Полное наименование Колледжа: Колледж программирования и кибербезопасности
	- Сокращенное наименование: КПК
	- Наименование Колледжа на английском языке: Сollege of programming and cyber security
	- Адрес местонахождения: Москва, 1-Щипковский переулок, д. 23.

	<b>Информация о ВУЗ'е</b>:
	- Полное наименование образовательной организации: Федеральное государственное бюджетное образовательное учреждение высшего образования "МИРЭА - Российский технологический университет"
	- Сокращенное наименование образовательной организации: РТУ МИРЭА

	<b>Специальности</b>:
	1) <b>09.02.01</b> Компьютерные системы и комплексы
	2) <b>09.02.03</b> Программирование в компьютерных системах
	3) <b>09.02.06</b> Сетевое и системное администрирование
	4) <b>09.02.07</b> Информационные системы и программирование
	5) <b>10.02.04</b> Обеспечение информационной безопасности телекоммуникационных систем
	6) <b>10.02.05</b> Обеспечение информационной безопасности автоматизированных систем
	7) <b>11.02.15</b> Инфокоммуникационные сети и системы связи
	8) <b>12.02.05</b> Оптические и оптико-электронные приборы и системы
	9) <b>12.02.09</b> Производство и эксплуатация оптических и оптикоэлектронных приборов и систем

	<b>Время проведения занятий</b>:
	<b>1 пара</b> – 8:45-10:15
	<b>2 пара</b> – 10:25-11:55
	<b>3 пара</b> – 12:30-14:00
	<b>4 пара</b> – 14:35-16:05
	<b>5 пара</b> – 16:15-17:45
	"""
	
	await message.answer(text=inf_general, parse_mode="html", reply_markup=bttns)
	logging.info(f"Information was sent successfully, user={message.from_user}, time={datetime.datetime.now()}")


def register_handlers_informer(dp : Dispatcher):
	dp.register_message_handler(giving_information, text=['🧷Инфо', 'Инфо', 'info'])
