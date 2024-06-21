from aiogram.types import (
   Message,
   InlineKeyboardMarkup,
   InlineKeyboardButton,
   ReplyKeyboardMarkup,
   KeyboardButton)
form_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="перейти к анкете")]
    ]
)
menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")]
    ]
)
menu_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Природа")]
    ]
)
menu_button_nature = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="море")],
                [KeyboardButton(text="горы")],
                [KeyboardButton(text="космос")]
            ]
        )
menu_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Люди")]
    ]
)
menu_button_people = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="спортсмены")],
                [KeyboardButton(text="дети")],
                [KeyboardButton(text="звёзды")]
            ]
        )
menu_button3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Техника")]
    ]
)
menu_button_technic = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="автомобили")],
                [KeyboardButton(text="мотоциклы")],
                [KeyboardButton(text="роботы")]
            ]
        )

menu_points = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="природа")],
                [KeyboardButton(text="люди")],
                [KeyboardButton(text="техника")],
                [KeyboardButton(text="другое")]
            ]
        )

random_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Бросить кубик и вывести другое изображение")]
    ]
)
