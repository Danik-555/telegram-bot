from aiogram.types import (Message)
from aiogram.filters import Command
from aiogram import Router

router = Router()

@router.message(Command("help"))
async def help(message: Message):
    text = "/start - запустить бота\n/help - показать доступные команды\n/menu - запустить меню"
    await message.answer(text=text)
    await message.delete()