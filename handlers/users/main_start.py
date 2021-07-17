# - *- coding: utf- 8 - *-
#
from handlers.users.admin_functions import send_message_to_user
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.foto_id import *
from filters import IsWork, IsUser
from filters.all_filters import IsBuy
from keyboards.default import check_user_out_func
from keyboards.inline import cicada
from loader import dp, bot
from states import StorageUsers
from utils.db_api.sqlite import *
from utils.other_func import get_dates
import datetime
import random
import time
import json
import requests
import sys

import urllib.request

import sqlite3
import os
import functions as func

fit = "AgACAgQAAxkBAAIEsWDwafGPgI5-QbmB4cg6MssyBx2SAAKItjEbJW2IU8QL1Ds17Nen"
url = ('http://telegra.ph//file/db14d05e947eb8784ec4d.jpg')
prohibit_buy = ["xbuy_item", "not_buy_items", "buy_this_item", "buy_open_position", "back_buy_item_position",
                "buy_position_prevp", "buy_position_nextp", "buy_category_prevp", "buy_category_nextp",
                "back_buy_item_to_category", "buy_open_category"]


# Проверка на нахождение бота на технических работах
@dp.message_handler(IsWork(), state="*")
@dp.callback_query_handler(IsWork(), state="*")
async def send_work_message(message: types.Message, state: FSMContext):
    if "id" in message:
        await message.answer("🔴 Бот находится на технических работах.")
    else:
        await message.answer("<b>🔴 Бот находится на технических работах.</b>")


# Обработка кнопки "На главную" и команды "/start"
@dp.message_handler(text="⬅ На главную", state="*")
@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    chat_id = (message.chat.id)
    first_name = (message.from_user.first_name)
    get_user_id = get_userx(user_id=message.from_user.id)
    if get_user_id is None:
        if message.from_user.username is not None:
            get_user_login = get_userx(user_login=message.from_user.username)
            if get_user_login is None:
                add_userx(message.from_user.id, message.from_user.username.lower(), first_name, 0, 0, get_dates())
            else:
                delete_userx(user_login=message.from_user.username)
                add_userx(message.from_user.id, message.from_user.username.lower(), first_name, 0, 0, get_dates())
        else:
            add_userx(message.from_user.id, message.from_user.username, first_name, 0, 0, get_dates())
    else:
        if first_name != get_user_id[3]:
            update_userx(get_user_id[1], user_name=first_name)
        if message.from_user.username is not None:
            if message.from_user.username.lower() != get_user_id[2]:
                update_userx(get_user_id[1], user_login=message.from_user.username.lower())
        await message.answer(f"{fmt.hide_link('http://telegra.ph//file/db14d05e947eb8784ec4d.jpg')}\n"
            f"      🔥Наш Магаз🔥\n "
            f"  ⚠️МЫ - КОМАНДА ЛИДЕРОВ⚠️\n "
            f"😈Ваш позитив - наша работа😈\n"
            f"    🔥Любой ⓝⓐⓡⓚⓞⓣⓘⓚ🔥\n "
            f"     🔥есть для вас 🔥\n"
            f"    🍀Ꮑน∂εᎮӹ ກᎮо∂αӜ🍀\n" 
            f"   🔥наша бдительность🔥\n"
            f"   🔥ваше  спокойствие🔥\n"
            f"  🏆ПОДАРИ ДУШЕ ДЖЕКПОТ🏆\n", parse_mode=types.ParseMode.HTML, 
                reply_markup=check_user_out_func(message.from_user.id))


@dp.message_handler(IsUser(), state="*")
@dp.callback_query_handler(IsUser(), state="*")
async def send_user_message(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,
                           "<b>❗ Ваш профиль не был найден.</b>\n"
                           "▶ Введите /start")


# Проверка на доступность покупок
@dp.message_handler(IsBuy(), text="🎁 Купить", state="*")
@dp.message_handler(IsBuy(), state=StorageUsers.here_input_count_buy_item)
@dp.callback_query_handler(IsBuy(), text_startswith=prohibit_buy, state="*")
async def send_user_message(message, state: FSMContext):
    if "id" in message:
        await message.answer("🔴 Покупки в боте временно отключены", True)
    else:
        await message.answer("<b>🔴 Покупки в боте временно отключены</b>")
       

