from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from keyboard.default_keyboard import main_menu, Ariza_qoldiring, Til, rus_vvv

router = Router()


@router.message(F.text == "🇷🇺/🇺🇿 Tilni tanlang")
async def send_start(message: types.Message):
    await message.answer(text="""🇷🇺/🇺🇿 Tilni tanlang""",
                         reply_markup=Til())


@router.message(F.text == "🇷🇺/🇺🇿 Выберите язык")
async def send_start(message: types.Message):
    await message.answer(text="""🇷🇺/🇺🇿 Выберите язык""",
                         reply_markup=Til())


@router.message(F.text == "🇷🇺")
async def send_start(message: types.Message):
    await message.answer(text="""🇷🇺/🇺🇿 Tilni tanlang""",
                         reply_markup=rus_vvv())


@router.message(F.text == "🇺🇿")
async def send_start(message: types.Message):
    await message.answer(text="""🇷🇺/🇺🇿 Tilni tanlang""",
                         reply_markup=main_menu())