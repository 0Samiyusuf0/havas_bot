from aiogram import Router
from . import start, help, about_us, beck, ariza, kontact, Til


def setup_message_router():
    router = Router()
    router.include_router(start.router)
    router.include_router(help.router)
    router.include_router(about_us.router)
    router.include_router(beck.router)
    router.include_router(ariza.router)
    router.include_router(kontact.router)
    router.include_router(Til.router)
    return router