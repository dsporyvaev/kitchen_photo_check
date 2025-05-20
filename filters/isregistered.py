from aiogram.filters import Filter
from aiogram import types
from aiogram.types import Message, Update

from services.api_sqlite import get_userx
from data.config import admins



class IsRegistered(Filter):
    async def __call__(self, event: Update):
        return get_userx(user_id = event.from_user.id)['user_login'] != ""