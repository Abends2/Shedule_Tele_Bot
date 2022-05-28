from aiogram import types, Dispatcher
from create_bot import dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from keyboards import bttns, group
from openpyxl import load_workbook # pandas
import logging
import datetime

logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)


# need for State
class Group(StatesGroup):
	student_group = State()


# ---------- /shedule ----------
# @dispatcher.message_handler(commands='shedule', state=None)
async def say_group(message: types.Message, state: FSMContext):
	await message.answer(text="Выбери в меню свою группу", reply_markup=group)
	await Group.student_group.set()


# ---------- /shedule : State ----------
# @dispatcher.message_handler(state=Group.student_group)
async def giving_shedule(callback : types.CallbackQuery, state: FSMContext):
	data = callback.data 	# getting callback_data from InlineKeyboard
	await state.update_data(answer=data)

	try:
		book = load_workbook(filename="./files/shedule.xlsx")
		sheet = book["Shedule"]
	except FileNotFoundError:
		await callback.message.answer(text='Прости, я не нашел файл. Мой администратор вскоре исправит ситуацию)\n', reply_markup=bttns)
		await state.finish()
		logging.info(f"File Not Found, time={datetime.datetime.now()}")

	groups = {'ИБ-21' : 'A', 'ИБ-22': 'B', 'ИБ-23': 'C'}
	result = ''

	try:
		if data in groups:
			for i in range(1, 32):
				cell = sheet[groups[data] + str(i)].value
				if ";" in cell:
					cell = cell[0:cell.find(";") + 1] + '\n' + '   ' + cell[cell.find(";") + 2:]
				result += cell + '\n'
		elif data != "Отмена":
			await callback.message.answer(text='Прости, я не нашел файл. Мой администратор вскоре исправит ситуацию)\n', reply_markup=bttns)
			logging.info(f"Shedule function was canceled, time={datetime.datetime.now()}")
		else:
			logging.info(f"Wrong variable data, time={datetime.datetime.now()}")
	finally:
		pass

	if data != "Отмена":
		await callback.message.answer(text=result, reply_markup=bttns)
		await callback.message.answer(text="Жду дальнейших указаний", reply_markup=bttns)
		await callback.answer()
		await state.finish()
		logging.info(f"Shedule was sent successfully, time={datetime.datetime.now()}")
	elif data == "Отмена" or data == False or data == '':
		await callback.message.answer("Жду других команд")
		await callback.answer()
		await state.finish()
		logging.info(f"Exit from StatesGroup, time={datetime.datetime.now()}")
	else:
		await state.finish()
		logging.info(f"User's group wasn't found, time={datetime.datetime.now()}")


def register_handlers_shedule(dp: Dispatcher):
	dp.register_message_handler(say_group, text=['📌Расписание', 'Расписание', 'shedule'], state=None)
	dp.register_callback_query_handler(giving_shedule, state=Group.student_group)