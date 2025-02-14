from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from keyboard.default_keyboard import main_menu
from keyboard.inline_keyboard import media_inline

router = Router()


@router.message(F.text == "📞 Kontaktlar")
async def send_start(message: types.Message):
    await message.answer_photo(photo="https://havasfood.uz/wp-content/uploads/2020/12/untitled-2-1.jpg",
                               caption="""🤝Muloqot uchun:
☎️Muloqot uchun +998 71 205 95 95
📩Elektron pochta havas_uz@mail.ru""",
                               reply_markup=media_inline())


@router.message(F.text == "📞 Нащи Крнтакты")
async def send_start(message: types.Message):
    await message.answer_photo(photo="https://havasfood.uz/wp-content/uploads/2020/12/untitled-2-1.jpg",
                               caption="""🤝Для связи:
☎️Для связи +998 71 205 95 95.
📩 Электронная почта havas_uz@mail.ru""",
                               reply_markup=media_inline())
