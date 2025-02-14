from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from keyboard.default_keyboard import main_menu, Ariza_qoldiring, Ariza_qoldiring2, fea

router = Router()


@router.message(F.text == "💬 Qayta aloqa")
async def send_start(message: types.Message):
    await message.answer(text="""Bizaga yoz va biza sizga jovobini beraviz""",
                         reply_markup=fea())
