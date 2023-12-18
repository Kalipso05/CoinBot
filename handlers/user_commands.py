from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keybords.main_kb import main_keyboard
from aiogram.types.dice import DiceEmoji
from states.state import Game
from aiogram.fsm.context import FSMContext
from database import users_bd
import asyncio
import random

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Добро пожаловать в CoinBot. Зарабывайте коины и обменивайте на разные плюшки", reply_markup=main_keyboard)
    if await users_bd.sqlite_check_user(message.from_user.id):
        print('В бД есть')
    else:
        await users_bd.sqlile_add_user(message.from_user.id)
    

@router.message(F.text == "🎮 Играть")
async def cmd_start_game(message: Message, state: FSMContext) -> None:
    await message.delete()
    await state.set_state(Game.count)
    await message.answer("Выберите число от 1-6, если угадаете, то Вы побеждаете")
    
@router.message(Game.count)
async def game(message: Message, state: FSMContext) -> None:
    await message.delete()
    dice_count = await message.answer_dice(DiceEmoji.DICE)
    await asyncio.sleep(3)
    coin_count = random.randint(1, 5)
    if message.text == str(dice_count.dice.value):
        await message.answer(f"🎉 Поздравляю, Вы победили!\nВаше загадонное число {message.text}\nЧисло которое выпало {dice_count.dice.value}\n\n🪙 В качестве приза вы выигрываете {coin_count} коин(ов)")
        await users_bd.sqlite_add_money(coin_count, message.from_user.id)
    else:
        await message.answer(f"Ты проиграл\nТвое загадонное число {message.text}\nЧисло которое выпало {dice_count.dice.value}\n\nТы мог бы выиграть {coin_count} коин(ов)")
    await state.clear()

@router.message(F.text == "👤 Пользователь")
async def cmd_start_game(message: Message) -> None:
    await message.delete()
    user_money = await users_bd.sqlite_get_data(message.from_user.id, "money")
    
    
    SHOW_USER_INFO = f"🆔 Ваш индитификатор: {message.from_user.id}\n🚹 Ваше имя: {message.from_user.first_name}\n\n🪙 Ваш баланс: {user_money[0]}"
    
    await message.answer(SHOW_USER_INFO)
