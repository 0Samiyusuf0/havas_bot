from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio
from handler import setup_message_router

API_TOKEN = "7869549413:AAEgDItq3Vrmn6NRxmDEcBbesPEZrXVZclY"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def on_startup(dispatcher: Dispatcher):
    await bot.send_message(chat_id="6682408679", text="Bot ishga tushdi")


async def main():
    dp.startup.register(on_startup)
    handler_router = setup_message_router()
    dp.include_router(handler_router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
