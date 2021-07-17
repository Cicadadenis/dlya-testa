# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup


def get_functions_func(user_id):
    functions_default = ReplyKeyboardMarkup(resize_keyboard=True)
    functions_default.row("📱 Поиск профиля 🔍", "📢 Рассылка", "📃 Поиск чеков 🔍")
    functions_default.row("👤 Добавление Администраторов ⚜️")
    functions_default.row("⬅ На главную")
    return functions_default
