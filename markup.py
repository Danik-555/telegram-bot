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

link_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Телеграм", url="https://t.me/MonsterDanik")],
            [InlineKeyboardButton(text="Сайт", url="https://www.google.com/")],
            [InlineKeyboardButton(text="информация об обоях", url="https://www.google.com/")]
        ]
)
menu_points = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="природа")],
                [KeyboardButton(text="люди")],
                [KeyboardButton(text="техника")]
            ]
        )


