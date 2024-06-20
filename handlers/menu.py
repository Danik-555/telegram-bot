from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu, Buttons
from re import fullmatch
from markup import menu_button, menu_points, menu_button1, menu_button_nature, menu_button2, menu_button_people, menu_button_technic

from aiogram.types import (KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup)
from aiogram.filters import Command

router = Router()


@router.message(Command('menu'))
@router.message(Menu.to_menu)
async def menu(message: Message, state: FSMContext):
    dice = await message.answer_dice()
    print(dice.dice.value)
    print((message.text))
    if message.text == "Меню" or message.text == "/menu":
        await state.set_state(Menu.menu)
        text = "Меню:\n\n1) природа \n\n2) люди \n\n3) техника"
        await message.answer(text=text, reply_markup=menu_points)


@router.message(Menu.menu)
async def choice(message: Message, state: FSMContext):
    print(message.text)
    if message.text.lower() == "природа":
        await state.set_state(Menu.nature)
        text = "Природа:\n\n1) море \n\n2) горы \n\n3) космос"
        await message.answer(text=text, reply_markup=menu_button_nature)
    if message.text.lower() == "люди":
        await state.set_state(Menu.people)
        text = "Люди:\n\n1) спортсмены \n\n2) дети \n\n3) звёзды"
        await message.answer(text=text, reply_markup=menu_button_people)
    if message.text.lower() == "техника":
        await state.set_state(Menu.technic)
        text = "Техника:\n\n1) автомобили \n\n2) мотоциклы \n\n3) роботы"
        await message.answer(text=text, reply_markup=menu_button_technic)


