"""
init handlers
"""
from aiogram import Router

from aiogram.filters import CommandStart

from handler import start
from filters import ChatTypeFilter


def prepare_router() -> Router:
    """
    prepare the router that's responsible to handle requests.
    """
    user_router = Router()
    user_router.message.filter(ChatTypeFilter("private"))
    user_router.message.register(start.command_start_handler, CommandStart())
    return user_router
