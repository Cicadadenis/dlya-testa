# - *- coding: utf- 8 - *-
#
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsWork, IsUser
from filters.all_filters import IsBuy
from keyboards.default import check_user_out_func
from loader import dp, bot
from states import StorageUsers
from utils.db_api.sqlite import *
from utils.other_func import get_dates






@dp.message_handler(content_types=["photo"])
async def download_photo(message: types.Message):
   # await message.photo[-1].download(destination="/")
    file_id = message.photo[-1].file_id
    await message.reply('Фото загруженно')
    await message.reply(file_id)
