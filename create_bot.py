from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# main object of our bot
bot = Bot(token='5224591766:AAEusyMiqE_lkFESzCS58w9bPCYyMHt8S3s')
# dispatcher for shedule_KPK_bot
dispatcher = Dispatcher(bot, storage=MemoryStorage())