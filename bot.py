# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import executor, types
from create_bot import dispatcher, bot
import logging

from handlers import date_scraper, giving_file, informer, shedule
from keyboards import bttns

# logs will be ON
logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

# for fast change a list of commands
cmd_strings = '/start\n/help\n/information\n/shedule\n/week\n/title\n/about_me'

async def on_startup(_):
	logging.info("Bot activated")

# need enter "/" before using a command
# ---------- /start ----------
@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.answer(text=f'Привет, {message.from_user.first_name}! Я - shedule KPK bot. Вот список моих команд:\n' + cmd_strings, reply_markup=bttns)
		logging.info("Greeted successfully")


@dispatcher.message_handler(commands=['help'])
async def helping(message: types.Message):
	await message.answer(text='Список доступных команд:\n' + cmd_strings, reply_markup=bttns)
	logging.info("Bot helped his user")


@dispatcher.message_handler(commands=['about_me'])
async def about(message: types.Message):
	await message.answer(text='Мой создатель: @maybeAbends\nПо всем вопросам и предложениям писать на почту: bilishbilli@gmail.com\nТвои друзья могут меня найти как: @G59_test_bot', reply_markup=bttns)


date_scraper.register_handlers_date_scraper(dispatcher)
giving_file.register_handlers_giving_file(dispatcher)
informer.register_handlers_informer(dispatcher)
shedule.register_handlers_shedule(dispatcher)


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False, on_startup=on_startup)