from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Переглянути паролі')],
    [KeyboardButton(text='Згенерувати пароль')]
], resize_keyboard=True, input_field_placeholder='Оберіть пункт меню')