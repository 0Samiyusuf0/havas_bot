from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from keyboard.default_keyboard import main_menu, Ariza_qoldiring, Ariza_qoldiring2

router = Router()


@router.message(F.text == "💼 Ariza qoldiring")
async def send_start(message: types.Message):
    await message.answer(text="""Sizni rezyumeingizni to'ldirishni boshlaymiz
📍 Viloyatni tanlang""",
                         reply_markup=Ariza_qoldiring())


@router.message(F.text == "💼 Подать заявку")
async def send_start(message: types.Message):
    await message.answer(text="""Мы поможем вам начать заполнять резюме
📍Выберите регион """,
                         reply_markup=Ariza_qoldiring2())