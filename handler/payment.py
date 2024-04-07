"""
the payment processing handlers
"""
import logging

from aiogram import Bot, types


logger = logging.getLogger(__name__)


async def process_pre_checkout_query(
    pre_checkout_query: types.PreCheckoutQuery,
    bot: Bot,
):
    """
    process pre-checkout query.
    """
    # add your logics here that's maybe database logics too for checking order already paid or not. # noqa
    order_id = pre_checkout_query.invoice_payload
    logger.info("processing pre-checkout query for order_id: %s", order_id)

    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message) -> None:
    """
    handler will forward receive a message back to the sender
    """
    chat_id = message.chat.id
    await message.bot.send_message(
        chat_id=chat_id,
        text=f"✅ Your order has been received. \n\nYour order id is {message.successful_payment.invoice_payload}"  # noqa
    )
