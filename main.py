import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from Bot_Function import  router

bot = Bot(token = '7702083419:AAFtAyyHHrOqB__eGuPsliF2ACJ-g7JPi8Q')
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
#print("Bot release soon")