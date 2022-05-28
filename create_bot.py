from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Main object of bot
bot = Bot(token='5224591766:AAEusyMiqE_lkFESzCS58w9bPCYyMHt8S3s')

# Dispatcher for bot
dispatcher = Dispatcher(bot, storage=MemoryStorage())