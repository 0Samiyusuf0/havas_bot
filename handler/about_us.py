from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import FSInputFile

from keyboard.default_keyboard import main_menu, Biz_haqimizda, Biz_haqimizda2


router = Router()


@router.message(F.text == "🏢 Biz haqimizda")
async def send_start(message: types.Message):
    video = FSInputFile("media/video/#HAVAS_Ниҳоят,_ролигимизнинг_«to_be_давоми»_😎.mp4")
    await message.answer_video(video=video,
        caption="""🌠HAVAS

📌"UYDA" CHEGIRMA DO'KON TARMOQI
Biz mijozlarimizga sifatli mahsulotlarni raqobatbardosh narxlarda taklif etamiz. Bizning do'konlarimizda taniqli jahon va mahalliy brendlar, shuningdek, o'zimiz ishlab chiqargan mahsulotlar taklif etiladi.""",
                         reply_markup=Biz_haqimizda())

@router.message(F.text == "🏢 Про нас")
async def send_start(message: types.Message):
        video = FSInputFile("media/video/#HAVAS_Ниҳоят,_ролигимизнинг_«to_be_давоми»_😎.mp4")
        await message.answer_video(video=video,
                                   caption="""🌠HAVAS

📌СЕТЬ ДИСКАУНТЕРОВ "У ДОМА"
Мы предлагаем нашим покупателям качественные продукты по выгодной цене. В наших магазинах представлены товары известных мировых и локальных брендов, а также товары собственного производства.""",
                                   reply_markup=Biz_haqimizda2())