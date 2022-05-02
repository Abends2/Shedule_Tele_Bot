from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

title_btn = KeyboardButton("/title")
inf_btn = KeyboardButton("/information")
start_btn = KeyboardButton("/start")
help_btn = KeyboardButton("/help")
shedule_btn = KeyboardButton("/shedule")
week_btn = KeyboardButton("/week")
about_btn = KeyboardButton('/about_me')

bttns = ReplyKeyboardMarkup(resize_keyboard=True).add(start_btn, help_btn, inf_btn, title_btn, shedule_btn, week_btn, about_btn)


ib21 = KeyboardButton("ИБ-21")
ib22 = KeyboardButton("ИБ-22")
ib23 = KeyboardButton("ИБ-23")

group = ReplyKeyboardMarkup(resize_keyboard=True).add(ib21, ib22, ib23)