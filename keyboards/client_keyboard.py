from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Main user's keyboard
main_page_btn = KeyboardButton("📃Титульник")
inf_btn = KeyboardButton("🧷Инфо")
start_btn = KeyboardButton("👋Старт")
help_btn = KeyboardButton("🆘Помощь")
shedule_btn = KeyboardButton("📌Расписание")
week_btn = KeyboardButton("📆Неделя")
about_btn = KeyboardButton('🤖О боте')

bttns = ReplyKeyboardMarkup(resize_keyboard=True).add(start_btn, help_btn, inf_btn, main_page_btn, shedule_btn, week_btn, about_btn)


ib21 = InlineKeyboardButton("ИБ-21", callback_data='ИБ-21')
ib22 = InlineKeyboardButton("ИБ-22", callback_data='ИБ-22')
ib23 = InlineKeyboardButton("ИБ-23", callback_data='ИБ-23')
exitbtn = InlineKeyboardButton("Отмена", callback_data='Отмена')

group = InlineKeyboardMarkup().add(ib21, ib22, ib23, exitbtn)
