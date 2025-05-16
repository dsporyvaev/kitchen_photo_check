from aiogram import Dispatcher, Bot, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
bot = Bot(token='8056380284:AAF2g23VNztgkqXe5J5LXVqpSieTZYU6fgU', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router = Router()
dp = Dispatcher()