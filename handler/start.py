from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from keyboard.default_keyboard import main_menu

router = Router()


@router.message(Command("start"))
async def send_start(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTS3BMwPn4PhdKgp1RHL9GDn0e1X9OlCJoChQ&s",caption="""Приветствую Вас, я HR-бот Havas

🤖Я:
- расскажу Вам о компании и о преимуществах работы у нас;
- помогу найти актуальные вакансии и заполнить анкету.

_______________________________________

Xush kelibsiz, men HR-bot Havas

🤖Men:
- sizga kompaniya haqida va biz bilan ishlashning afzalliklari haqida gapirib beraman;
- mavjud vakansiyalarni topishga va so'rovnomani to'ldirishga yordam beraman.""",
                         reply_markup=main_menu())