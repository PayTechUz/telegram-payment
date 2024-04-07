"""
default handler
"""
from aiogram import types


async def default_handler(message: types.Message) -> None:
    """
    default handler for unknown messages
    """
    await message.reply("Please choose a product and order it!")
