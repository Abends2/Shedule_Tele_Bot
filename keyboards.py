from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

title_btn = KeyboardButton("/title")
start_btn = KeyboardButton("/start")
shedule_btn = KeyboardButton("/shedule")
week_btn = KeyboardButton("/week")

bttns = ReplyKeyboardMarkup(resize_keyboard=True).add(start_btn, title_btn, shedule_btn, week_btn)