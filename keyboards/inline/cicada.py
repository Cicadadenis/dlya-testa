# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton





cicada3301 = InlineKeyboardMarkup()

cicada3301.row(
    InlineKeyboardButton(text='🏞 Получить id фото:', callback_data='id_foto')
)