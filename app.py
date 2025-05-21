import sys
import asyncio
import logging
from aiogram import Dispatcher
from bot_instance import bot
from handlers.admin.admin_handlers import admin_router
from handlers.user.handlers import legit_router
from handlers.user.user_registration import registration_router
from data.config import BOT_VERSION
from utils.set_bot_commands import set_default_commands
from middlewares.user_registered import RegisteredUserMiddleware
from services.api_sqlite import create_dbx
from handlers.user.mid_shift import mid_shift_router
from handlers.user.morning_shift import morning_shift_router
from handlers.user.night_shift import night_shift_router


def register_routers(disp:Dispatcher):
    disp.include_router(legit_router)
    disp.include_router(registration_router)
    disp.include_router(admin_router)
    disp.include_router(mid_shift_router)
    disp.include_router(morning_shift_router)
    disp.include_router(night_shift_router)

async def on_startup() -> None:
    await set_default_commands(bot)
    print("Bot started [+]")
    print(f"Version: {BOT_VERSION}")

async def on_shutdown() -> None:
    print("Bot shutdown")



async def main() -> None:

    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    legit_router.message.middleware(RegisteredUserMiddleware())
    register_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    create_dbx()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
