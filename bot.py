# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import executor, types
from create_bot import dispatcher, bot
import logging
import emoji

from handlers import date_scraper, giving_file, informer, shedule
from keyboards import bttns

# need enter "/" before using a command

# logs will be ON
logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

# a list of commands
cmd_strings = '''-------------------	
/start - Приветствие
/help - Вывести список доступных команд
/information - Показать информацию о Колледже и ВУЗ'e
/shedule - Подсказать расписание для конкретной группы
/week - Вывести сегодняшнее число и неделю обучения
/main_page - Выдать word-файл с титульным листом
/about_me - Доп. информация о боте
-------------------'''


async def on_startup(_):
	logging.info("Bot activated")


# ---------- /start ----------
@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.answer(text=f'Привет, {message.from_user.first_name}' + emoji.emojize(":fire:") + emoji.emojize(":handshake:") + '\n' + 'Я - <b>shedule KPK bot</b>. Нажми /help, чтобы посмотреть, что я умею', parse_mode="html", reply_markup=bttns)
		logging.info("Greeted successfully")


# ---------- /help ----------
@dispatcher.message_handler(commands=['help'])
async def helping(message: types.Message):
	await message.answer(text=emoji.emojize(":check_mark_button:") + 'Список доступных команд:\n' + cmd_strings, reply_markup=bttns)
	logging.info("Bot helped his user")


# ---------- /about_me ----------
@dispatcher.message_handler(commands=['about_me'])
async def about(message: types.Message):
	await message.answer(text='Мой создатель: (AUTHOR\'s TELEGRAM)\nПо всем вопросам и предложениям писать на почту: example@gmail.com\nТвои друзья могут меня найти как: (BOT_URL_WITH_@)', reply_markup=bttns)
	logging.info("Bot told about himself")


date_scraper.register_handlers_date_scraper(dispatcher)
giving_file.register_handlers_giving_file(dispatcher)
informer.register_handlers_informer(dispatcher)
shedule.register_handlers_shedule(dispatcher)


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False, on_startup=on_startup)