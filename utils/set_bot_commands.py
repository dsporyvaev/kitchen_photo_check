from aiogram import types, Bot
from aiogram.methods.set_my_commands import SetMyCommands
async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand(command='/start', description='Start bot'),
        types.BotCommand(command='/help', description='See all commands'),
        types.BotCommand(command='/register', description='Start registration process')
    ])