from aiogram.fsm.context import FSMContext
from aiogram.types import (Message)
from aiogram.filters import Command
from aiogram import Router
from states import Commands
router = Router()

@router.message(Command("help"))
async def help(message: Message, state: FSMContext):
    await state.set_state(Commands.commands)
    text = "/start - запустить бота\n/help - показать доступные команды\n/menu - запустить меню"
    await message.answer(text=text)
    await message.delete()

@router.message(Commands.commands)
async def help1(message: Message, state: FSMContext):
    if message.text not in ["/start, /help, /menu"]:
        await message.answer(text="/start - запустить бота\n/help - показать доступные команды\n/menu - запустить меню")
