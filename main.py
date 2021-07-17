# - *- coding: utf- 8 - *-
import asyncio

from aiogram import executor

import filters
import middlewares
from handlers import dp
from utils.db_api.sqlite import create_bdx
from utils.other_func import on_startup_notify,  check_update_bot
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    filters.setup(dp)
    middlewares.setup(dp)

    await set_default_commands(dp)
    await on_startup_notify(dp)

    #asyncio.create_task(check_update_bot())
    print("~~~~~ Бот был запущен ~~~~~")


if __name__ == "__main__":
    create_bdx()
    executor.start_polling(dp)
