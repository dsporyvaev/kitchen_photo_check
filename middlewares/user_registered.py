

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Update, Message
from data.config import admins
from services.api_sqlite import add_userx, add_user_lastname, add_user_name, get_userx
from typing import Callable, Awaitable, Any, Dict
from keyboards.default.keyboard_menu import kb_register


class RegisteredUserMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str,Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str,Any]
    ) -> Any:
        this_user = event.from_user
        user_id = this_user.id
        user_name = this_user.username

        get_user = get_userx(user_id=user_id)
        if event.text == '/help' and get_user is None:
            await event.answer("This is testbot, now youre not registered, to register: /register")
        if event.text == '/start' and get_user is None:
            await event.answer("You're not registered yet, to register: /register")
        if get_user is None:
            add_userx(user_id, user_login="")
            print("didnt exist, User added")
            return await event.answer(text="user was added")

        elif get_user['user_login'] == "":
            return await event.answer(text="You didn`t registered, first need to register", reply_markup=kb_register)


        else:
            print("else")
            return await handler(event, data)