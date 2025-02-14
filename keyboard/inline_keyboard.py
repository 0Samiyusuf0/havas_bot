from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def media_inline():
    button = InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/havasuz/")
    button2 = InlineKeyboardButton(text="Web-site", url="https://havasfood.uz/")
    button3 = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/havasuz/")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button3],

        ]
    )
    return ikm