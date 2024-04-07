"""
the start handler implementation.
"""
from aiogram.types import Message
from aiogram.utils.markdown import hbold


from shortcut import constructor


async def command_start_handler(message: Message) -> None:
    """
    hhis handler receives messages with `/start` command
    """
    text = f"Hello, {hbold(message.from_user.full_name)}!"
    buttons = constructor.create_kb(["🛍 Products"], [1])

    await message.answer(text, reply_markup=buttons)
