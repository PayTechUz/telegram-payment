"""
the products page
"""
import uuid
import logging

from aiogram import types

from conf import get_provider_token


logger = logging.getLogger(__name__)


async def product_handler(message: types.Message) -> None:
    """
    product handler that returns products list of products
    """
    chat_id = message.chat.id

    # product info
    product_currency = "UZS"
    product_title = "Chicken foot, a beloved delicacy in Caribbean and Southern U.S" # noqa
    product_description = "Chicken foot, a beloved delicacy in Caribbean and Southern U.S. cuisine, offers a unique culinary experience. Marinated in a flavorful blend of spices and seasonings, these chicken feet boast a rich taste and tantalizing texture" # noqa
    product_photo_url = "https://i.pinimg.com/originals/31/a3/cf/31a3cfae922924cfa1c358eb459f02cd.jpg" # noqa
    product_amount = 42000
    product_start_parameter = "time-machine-example"
    product_payload = uuid.uuid4()

    await message.bot.send_invoice(
        chat_id=chat_id,
        currency=product_currency,
        title=product_title,
        description=product_description, # noqa
        provider_token=get_provider_token("click"),
        is_flexible=False,
        photo_url=product_photo_url,
        prices=[
            types.LabeledPrice(
                label='Amount',
                amount=product_amount
            )
        ],
        start_parameter=product_start_parameter,
        payload=str(product_payload)
    )
