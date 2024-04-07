"""
aiogram payment example with payze.io
"""
import sys
import asyncio
import logging

from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

from conf import BOT_TOKEN
from router import prepare_router

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()


async def main() -> None:
    """
    Initialize Bot instance with a default parse
    mode which will be passed to all API calls
    """
    dp.include_routers(prepare_router())
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
