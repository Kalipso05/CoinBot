from aiogram import Bot, Dispatcher, Router
from handlers import user_commands
from database.users_bd import sqlitedb_start
import asyncio


async def start_bot():
    sqlitedb_start()
    bot = Bot(token="")
    dp = Dispatcher()
    dp.include_router(user_commands.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(start_bot())
