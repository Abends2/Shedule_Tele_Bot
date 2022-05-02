from aiogram import types, Dispatcher
from create_bot import dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards import bttns, group
from openpyxl import load_workbook
import logging

logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)


# need for State
class Group(StatesGroup):
	student_group = State()


# ---------- /shedule ----------
# @dispatcher.message_handler(commands='shedule', state=None)
async def say_group(message: types.Message, state: FSMContext):
	await message.answer(text="Выбери в меню свою группу", reply_markup=group)
	await Group.student_group.set()


# @dispatcher.message_handler(state=Group.student_group)
async def giving_shedule(message: types.Message, state: FSMContext):
	data = message.text
	print(data)
	await state.update_data(answer=data)

	book = load_workbook(filename="./files/shedule.xlsx")
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
	else:
		print("No data")

	if data:
		try:
			await message.answer(text=result, reply_markup=bttns)
			logging.info("Shedule was sent successfully")
		except FileNotFoundError:
			await message.answer(text='Прости, я не нашел файл. Мой администратор (надеюсь) вскоре исправит ситуацию)\n' + cmd_strings, reply_markup=bttns)
			logging.info("File Not Found")
	else:
		print("Группа не найдена")
		
	await state.finish()


def register_handlers_shedule(dp: Dispatcher):
	dp.register_message_handler(say_group, commands=['shedule'], state=None)
	dp.register_message_handler(giving_shedule, state=Group.student_group)