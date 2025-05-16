import sys
import asyncio
import logging
from aiogram import Dispatcher
from bot_instance import bot
from handlers import user_router

def register_routers(disp:Dispatcher):
    disp.include_router(user_router)


async def main() -> None:
    dp = Dispatcher()

    register_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
