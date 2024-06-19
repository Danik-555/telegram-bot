from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu, Buttons
from aiogram.types import Message, InputMediaPhoto


router = Router()


@router.message(Menu.technic)
async def choice2(message: Message, state: FSMContext):
    if message.text.lower() == "автомобили":
        await state.set_state(Buttons.button_car)
        images = [InputMediaPhoto(media="AgACAgIAAxkBAAIEUGZupIDd-lv7z4CXZwgYgUA4gyxSAAL-2zEb7o5wS44rr0q_RuERAQADAgADeQADNQQ")]
        await message.answer_media_group(media=images)
    if message.text.lower() == "мотоциклы":
        await state.set_state(Buttons.button_car1)
        images = [InputMediaPhoto(
            media="AgACAgIAAxkBAAIGQWZv6ldEb2ekJXD2InQ8wAIZEbdcAAJ-1zEbRIyAS5OrUpiTfAJtAQADAgADeQADNQQ")]
        await message.answer_media_group(media=images)
        await message.delete()