from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import  keyboard as key_board_

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привіт! Розпочнемо роботу!', reply_markup = key_board_.main_keyboard)


