import asyncio
import os
from aiogram import Bot, Dispatcher
from admin import permission_for_toggle, permission_for_disable_order_songs, ban_user, send_to_all, change_dj
from handlers import basic, order_song, put_like, send_review, radio_institute, is_swear, register, banned
from background import keep_alive


async def main():

    bot = Bot(token=os.environ['BOT_KEY'], parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(banned.router, register.router, is_swear.router, ban_user.router, change_dj.router, send_to_all.router, permission_for_toggle.router, permission_for_disable_order_songs.router,
                       order_song.router, put_like.router,
                       send_review.router, radio_institute.router,
                       basic.router)
    await bot.delete_webhook(drop_pending_updates=True)  # disable answering after shutdown
    await dp.start_polling(bot)


if __name__ == '__main__':

    keep_alive()
    asyncio.run(main())
