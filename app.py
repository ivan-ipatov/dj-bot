import asyncio
import os
import time

from aiogram import Bot, Dispatcher

from admin import request_for_toggle_event_mode, request_for_toggle_order_songs_mode, ban_user, \
    send_mailing_to_subscribes, change_dj
from background import keep_alive
from handlers import basic, order_song, put_like, send_review, radio_institute, swear, register, banned

"""
Main file of bot start up part 
"""


async def main():
    """
    Bot start up
    """
    bot = Bot(token=os.environ['BOT_KEY'], parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(banned.router, register.router, swear.router, ban_user.router, change_dj.router,
                       send_mailing_to_subscribes.router, request_for_toggle_event_mode.router,
                       request_for_toggle_order_songs_mode.router,
                       order_song.router, put_like.router,
                       send_review.router, radio_institute.router,
                       basic.router)
    await bot.delete_webhook(drop_pending_updates=True)  # disable answering after shutdown
    await dp.start_polling(bot)


def do_start_up():
    """
    Main function of start up
    """
    keep_alive()
    while True:
        try:
            if __name__ == '__main__':
                asyncio.run(main())
        except Exception as e:
            time.sleep(3)
            print(e)
