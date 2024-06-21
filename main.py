import asyncio

from handlers import form, help, start, menu

from aiogram import Bot
from config_reader import config
from aiogram.dispatcher.dispatcher import Dispatcher

from antiflood import AntiFloodMiddleware

from database import start_db

bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()


async def main():
    await start_db()
    dp.message.middleware(AntiFloodMiddleware())
    dp.include_routers(
        start.router,
        help.router,
        menu.router,
        form.router,

    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
