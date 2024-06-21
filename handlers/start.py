from aiogram.types import Message, FSInputFile, PollAnswer, InputMediaPhoto
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form

from database import check_profile
from handlers import form
from states import Form, Menu
from markup import form_button, menu_button


router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Form.wait)
    exists = await check_profile(message.from_user.id)
    if not exists:
        text = "Привет! Перед началом необходимо заполнить небольшую анкету. Нажми на кнопку ниже, чтобы перейти к заполнению!"
        await message.answer(text=text, reply_markup=form_button)
        await state.set_state(Form.wait)
    else:
        await message.answer(text= "Привет! Нажми на кнопку ниже, чтобы открыть меню", reply_markup=menu_button)
        await state.set_state(Menu.to_menu)
        await message.delete()







@router.poll_answer()
async def poll_answer(poll_answer: PollAnswer):
    answer_inds = poll_answer.options_ids
    print(answer_inds)

