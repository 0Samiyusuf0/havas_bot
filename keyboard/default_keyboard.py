from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    button = KeyboardButton(text="🏢 Biz haqimizda")
    button2 = KeyboardButton(text="💼 Ariza qoldiring")
    button3 = KeyboardButton(text="📞 Kontaktlar")
    button4 = KeyboardButton(text="w")
    button5 = KeyboardButton(text="🇷🇺/🇺🇿 Tilni tanlang")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2],
            [button3, button4],
            [button5],
        ],
        resize_keyboard=True
    )
    return rkm


def rus_vvv():
    button = KeyboardButton(text="🏢 Про нас")
    button2 = KeyboardButton(text="💼 Подать заявку")
    button3 = KeyboardButton(text="📞 Нащи Крнтакты")
    button4 = KeyboardButton(text="💬 Обратная связь")
    button5 = KeyboardButton(text="🇷🇺/🇺🇿 Выберите язык")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2],
            [button3, button4],
            [button5],
        ],
        resize_keyboard=True
    )
    return rkm


def Biz_haqimizda():
    button = KeyboardButton(text="🔰 Chegirma — bu")
    button2 = KeyboardButton(text="📍Yaqin Filial")
    button3 = KeyboardButton(text="⏎ back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm


def Biz_haqimizda2():
    button = KeyboardButton(text="🔰 Discaunt — это")
    button2 = KeyboardButton(text="📍Ближайший Филлиал")
    button3 = KeyboardButton(text="🔙 back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm




def Ariza_qoldiring():
    button = KeyboardButton(text="Bosh Offis")
    button2 = KeyboardButton(text="Sirdaryo")
    button3 = KeyboardButton(text="Toshkent")
    button4 = KeyboardButton(text="Toshkent Viloyati")
    button5 = KeyboardButton(text="⟳ back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm


def Ariza_qoldiring2():
    button = KeyboardButton(text="Главный Оффис")
    button2 = KeyboardButton(text="Сирдарья")
    button3 = KeyboardButton(text="Ташкент")
    button4 = KeyboardButton(text="Ташкентский Вилоят")
    button5 = KeyboardButton(text="⬅️ назад")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm


def Til():
    button = KeyboardButton(text="🇷🇺")
    button2 = KeyboardButton(text="🇺🇿")
    button3 = KeyboardButton(text="↩ back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm


def Til():
    button = KeyboardButton(text="🇷🇺")
    button2 = KeyboardButton(text="🇺🇿")
    button3 = KeyboardButton(text="↩ назад")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm


def fea():

    button3 = KeyboardButton(text="↩")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm