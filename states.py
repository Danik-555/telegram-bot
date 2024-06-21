from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    wait = State()
    name = State()
    age = State()
    email = State()
    favourite_colour = State()
    taste = State()
    telephone = State()

class Menu(StatesGroup):
    to_menu = State()
    menu = State()
    menu_points = State()
    menu_points2 = State()
    nature = State()
    people = State()
    technic = State()
    other = State()
    message = State()

class Buttons(StatesGroup):
    button_car = State()
    button_car1 = State()

class Commands(StatesGroup):
    commands = State()



