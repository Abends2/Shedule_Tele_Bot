from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn=KeyboardButton("/Hi")

greet = ReplyKeyboardMarkup(resize_keyboard=True).add(btn)
