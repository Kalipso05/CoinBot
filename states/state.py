from aiogram.fsm.state import State, StatesGroup

class Game(StatesGroup):
    count = State()
    rematch = State()