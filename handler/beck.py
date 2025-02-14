from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from keyboard.default_keyboard import main_menu, Ariza_qoldiring, rus_vvv

router = Router()


@router.message(F.text == "⏎ back")
async def send_start(message: types.Message):
    await message.answer(text="⏎ back",
                         reply_markup=main_menu())


@router.message(F.text == "⟳ back")
async def send_start(message: types.Message):
    await message.answer(text="⟳ back",
                         reply_markup=main_menu())


@router.message(F.text == "↩ back")
async def send_start(message: types.Message):
    await message.answer(text="↩ back",
                         reply_markup=main_menu())


@router.message(F.text == "🔙 back")
async def send_start(message: types.Message):
    await message.answer(text="🔙 back",
                         reply_markup=rus_vvv())


@router.message(F.text == "⬅️ назад")
async def send_start(message: types.Message):
    await message.answer(text="⬅️ назад",
                         reply_markup=rus_vvv())


@router.message(F.text == "↩ назад")
async def send_start(message: types.Message):
    await message.answer(text="↩ назад",
                         reply_markup=rus_vvv())


@router.message(F.text == "↩")
async def send_start(message: types.Message):
    await message.answer(text="↩",
                         reply_markup=main_menu())


@router.message(F.text == "⬅️")
async def send_start(message: types.Message):
    await message.answer(text="⬅️",
                         reply_markup=rus_vvv())
