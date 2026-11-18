from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Купить подписку", callback_data="buy")]
        ]
    )