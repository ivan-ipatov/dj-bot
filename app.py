import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import basic, order_song, put_like, send_review


async def main():
    bot = Bot(token=os.environ['BOT_KEY'], parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(order_song.router, put_like.router, send_review.router, basic.router)
    await bot.delete_webhook(drop_pending_updates=True) # disable answering after shutdown
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())