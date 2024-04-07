"""
init router
"""
from aiogram import Router
from aiogram.filters import CommandStart

from filters import chat
from filters import text
from filters.payment import SuccessfullyPayment

from handler import start
from handler import product
from handler import payment
from handler import default


def prepare_router() -> Router:
    """
    prepare routing
    """
    user_router = Router()
    user_router.message.filter(chat.ChatTypeFilter("private"))

    user_router.message.register(start.command_start_handler, CommandStart())
    user_router.message.register(product.product_handler, text.TextFilter("🛍 Products")) # noqa
    user_router.pre_checkout_query.register(payment.process_pre_checkout_query)
    user_router.message.register(payment.successful_payment, SuccessfullyPayment()) # noqa
    user_router.message.register(default.default_handler)

    return user_router
