from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command

from keyboards.inline import main_menu

user_router = Router()

@user_router.message(CommandStart()) 
def start(message: Message):
    message.answer(f"""Приветстую, {message.from_user.first_name}!
Для того что бы оплатить подписку воспользуйтесь кнопками. 👇
""", 
    reply_markup=main_menu())

