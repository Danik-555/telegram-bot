from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu
from re import fullmatch
from markup import menu_button
from database import create_profile, edit_profile

router = Router()



@router.message(Form.wait)
async def waiting(message: Message, state: FSMContext):
    print(1)
    await state.update_data(id=message.from_user.id)
    if message.text.lower() == "перейти к анкете":
        await state.set_state(Form.name)
        await message.answer("Введите имя")
    else:
        text = "Я тебя не понимаю :( Нажми на кнопку ниже, чтобы начать анкету"
        await message.answer(text=text)

@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        await message.answer("Отлично! Введите возраст")
    else:
        text = "Введите корректное имя!"
        await message.answer(text=text)



@router.message(Form.age)
async def age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age = message.text)
        await state.set_state(Form.email)
        await message.answer("Введи электронную почту")
    else:
        await message.answer("Введи корректный возраст")

@router.message(Form.email)
async def email(message: Message, state: FSMContext):
    if fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)", message.text):
        await state.update_data(email=message.text)
        data_dict = await state.get_data()
        await state.set_state(Menu.to_menu)
        await create_profile(data_dict['id'])
        await edit_profile(data_dict['id'], data_dict['name'], data_dict['age'], data_dict['email'])
        await message.answer(
            "Спасибо, анкета пройдена! Нажмите кнопку меню, чтобы продолжить",
            reply_markup=menu_button
        )
    else:
        await message.answer("Введи корректный адрес электронной почты")




