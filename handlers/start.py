from aiogram.types import Message, FSInputFile, PollAnswer, InputMediaPhoto
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form
from markup import form_button
from erg2 import get_photo

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Form.wait)
    text = "Привет! Перед началом необходимо заполнить небольшую анкету. Нажми на кнопку ниже, чтобы перейти к заполнению!"
    await message.answer(text=text, reply_markup=form_button)
    photo = await get_photo('имя фотографии')
    await message.answer_photo(media=photo)
    await message.delete()



@router.poll_answer()
async def poll_answer(poll_answer: PollAnswer):
    answer_inds = poll_answer.options_ids
    print(answer_inds)
