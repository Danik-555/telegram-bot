from aiogram.types import Message, InputMediaPhoto
from aiogram import Router
from aiogram.fsm.context import FSMContext


from states import Form, Menu, Buttons
from re import fullmatch
from markup import menu_button, menu_points, menu_button1, menu_button_nature, menu_button2, menu_button_people, \
    menu_button_technic, random_button

from aiogram.types import (KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup)
from aiogram.filters import Command
from erg2 import get_photo
router = Router()


@router.message(Command('menu'))
@router.message(Menu.to_menu)
async def menu(message: Message, state: FSMContext):
    if message.text == "Меню" or message.text == "/menu":
        await state.set_state(Menu.menu)
        text = ("Меню:\n\n1) природа \n\n2) люди \n\n3) техника \n\n4) другое")
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
    if message.text.lower() == "другое":
        await state.set_state(Menu.other)
        text = "Бросить кубик и вывести другое изображение"
        await message.answer(text=text, reply_markup=random_button)

@router.message(Menu.other)
async def cubic(message: Message, state: FSMContext):
    print(message.text)
    if message.text == "Бросить кубик и вывести другое изображение":
        await message.answer_dice()
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=random_button)
        images = [InputMediaPhoto(media=await get_photo("hippo")),
                  InputMediaPhoto(media=await get_photo("dog")),
                  InputMediaPhoto(media=await get_photo("frog"))]
        await message.answer_media_group(media=images)

@router.message(Menu.people)
async def choice_people(message: Message, state: FSMContext):
    if message.text.lower() == "спортсмены":
        await state.set_state(Menu.people)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_people)
        images = [InputMediaPhoto(media=await get_photo("sport1")),
                  InputMediaPhoto(media=await get_photo("sport2")),
                  InputMediaPhoto(media=await get_photo("sport3"))]
        await message.answer_media_group(media=images)
    if message.text.lower() == "дети":
        await state.set_state(Menu.people)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_people)
        images = [InputMediaPhoto(media=await get_photo("kids1")),
                  InputMediaPhoto(media=await get_photo("kids2")),
                  InputMediaPhoto(media=await get_photo("kids3"))]
        await message.answer_media_group(media=images)
    if message.text.lower() == "звёзды":
        await state.set_state(Menu.people)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_people)
        images = [InputMediaPhoto(media=await get_photo("stars1")),
                  InputMediaPhoto(media=await get_photo("stars2")),
                  InputMediaPhoto(media=await get_photo("stars3"))]
        await message.answer_media_group(media=images)



@router.message(Menu.nature)
async def choice_nature(message: Message, state: FSMContext):
    if message.text.lower() == "море":
        await state.set_state(Menu.nature)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_nature)
        images = [InputMediaPhoto(media=await get_photo("sea1")),
                  InputMediaPhoto(media=await get_photo("sea2")),
                  InputMediaPhoto(media=await get_photo("sea3"))]
        await message.answer_media_group(media=images)
    if message.text.lower() == "горы":
        await state.set_state(Menu.nature)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_nature)
        images = [InputMediaPhoto(media=await get_photo("mountain1")),
                  InputMediaPhoto(media=await get_photo("mountain2")),
                  InputMediaPhoto(media=await get_photo("mountain3"))]
        await message.answer_media_group(media=images)
    if message.text.lower() == "космос":
        await state.set_state(Menu.nature)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_nature)
        images = [InputMediaPhoto(media=await get_photo("space1")),
                  InputMediaPhoto(media=await get_photo("space2")),
                  InputMediaPhoto(media=await get_photo("space3"))]
        await message.answer_media_group(media=images)

@router.message(Menu.technic)
async def choice_nature(message: Message, state: FSMContext):
    if message.text.lower() == "автомобили":
        await state.set_state(Menu.technic)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_technic)
        images = [InputMediaPhoto(media=await get_photo("car2")),
                  InputMediaPhoto(media=await get_photo("car1")),
                  InputMediaPhoto(media=await get_photo("car3"))]
        await message.answer_media_group(media=images)
    if message.text.lower() == "мотоциклы":
        await state.set_state(Menu.technic)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_technic)
        images = [InputMediaPhoto(media=await get_photo("moto1")),
                  InputMediaPhoto(media=await get_photo("moto2")),
                  InputMediaPhoto(media=await get_photo("moto3"))]
        await message.answer_media_group(media=images)
    if message.text.lower() == "роботы":
        await state.set_state(Menu.nature)
        text = "Обои готовы:)"
        await message.answer(text=text, reply_markup=menu_button_technic)
        images = [InputMediaPhoto(media=await get_photo("robot1")),
                  InputMediaPhoto(media=await get_photo("robot2")),
                  InputMediaPhoto(media=await get_photo("robot3"))]
        await message.answer_media_group(media=images)



