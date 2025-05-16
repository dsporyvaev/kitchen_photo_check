import sys

from loader import dp, bot
import asyncio
import logging
async def on_startup():
     print("Bot started successfully")


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
