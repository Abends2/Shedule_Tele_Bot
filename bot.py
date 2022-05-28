# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import executor, types
from create_bot import dispatcher, bot
import logging
import emoji
import datetime

from handlers import date_scraper, giving_file, informer, shedule
from keyboards import bttns


# logs will be ON
logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

# a list of commands
cmd_strings = '''-------------------	
<b>Старт</b> - Приветствие
<b>Помощь</b> - Вывести список доступных команд
<b>Инфо</b> - Показать информацию о Колледже и ВУЗ'e
<b>Расписание</b> - Подсказать расписание для конкретной группы
<b>Неделя</b> - Вывести сегодняшнее число и неделю обучения
<b>Титульник</b> - Выдать word-файл с титульным листом
<b>О боте</b> - Доп. информация о боте
-------------------

❗️❗️Для простоты навигации, используй клавиатуру бота'''


async def on_startup(_):
	logging.info("Bot activated")


# ---------- /start ----------
@dispatcher.message_handler(text=['👋Старт', 'Старт', 'start'])
async def start(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.answer(text=f'Привет, {message.from_user.first_name}' + emoji.emojize(":fire:") + emoji.emojize(":handshake:") + '\n' + 'Я - <b>shedule KPK bot</b>. Нажми <b>Помощь</b>, чтобы посмотреть мои команды', parse_mode="html", reply_markup=bttns)
		logging.info(f"Greeted successfully, user={message.from_user}, time={datetime.datetime.now()}")


# ---------- /help ----------
@dispatcher.message_handler(text=['🆘Помощь', 'Помощь', 'help'])
async def helping(message: types.Message):
	await message.answer(text=emoji.emojize(":check_mark_button:") + 'Список доступных команд:\n' + cmd_strings, parse_mode= 'HTML', reply_markup=bttns)
	logging.info(f"Bot helped his user, user={message.from_user}, time={datetime.datetime.now()}")


# ---------- /about_me ----------
@dispatcher.message_handler(text=['🤖О боте', 'О боте', 'about bot'])
async def about(message: types.Message):
	await message.answer(text='Мой создатель: (AUTHOR\'s TELEGRAM)\nПо всем вопросам и предложениям писать на почту: example@gmail.com\nТвои друзья могут меня найти как: (BOT_URL_WITH_@)', reply_markup=bttns)
	logging.info(f"Bot told about himself, user={message.from_user}, time={datetime.datetime.now()}")


date_scraper.register_handlers_date_scraper(dispatcher)
giving_file.register_handlers_giving_file(dispatcher)
informer.register_handlers_informer(dispatcher)
shedule.register_handlers_shedule(dispatcher)


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False, on_startup=on_startup)