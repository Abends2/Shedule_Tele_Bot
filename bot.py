# ----- Author: Abends2 -----
# ----- Shedule KPK Bot -----

from aiogram import executor, types
from create_bot import dispatcher, bot
import logging

from handlers import date_scraper, giving_file, informer, keyboards, shedule

# logs will be ON
logging.basicConfig(filename="../logs/logs.txt", filemode='w', level=logging.INFO)

# for fast change a list of commands
cmd_strings = 'Use commands:\n/start\n/information\n/shedule\n/week\n/title'

async def on_startup(_):
	logging.info("Bot activated")

# need enter "/" before using a command
# ---------- /start ----------
@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
	try:
		me = await bot.get_me()
	finally:
		await message.answer(text=f'Hi, {message.from_user.first_name}, I\'m a shedule_KPK_bot.' + cmd_strings, reply_markup=keyboards.bttns)
		logging.info("Greeted successfully")

date_scraper.register_handlers_date_scraper(dispatcher)
giving_file.register_handlers_giving_file(dispatcher)
informer.register_handlers_informer(dispatcher)
shedule.register_handlers_shedule(dispatcher)


if __name__ == "__main__":
	# Start Bot
	executor.start_polling(dispatcher, skip_updates=False, on_startup=on_startup)