from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

router = Router()

# Команда /donate для отправки счета на Звезды
@router.message(Command("donate"))
async def cmd_donate(message: Message):
    prices = [LabeledPrice(label="Поддержка проекта", amount=1)]
    await message.answer_invoice(
        title="Донат разработчику",
        description="Поддержите бота и получите звезды на баланс!",
        payload="donate_stars_payload",
        currency="XTR",
        prices=prices,
        start_parameter="donate"
    )

# Подтверждение платежа
@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Успешная оплата
@router.message(F.successful_payment)
async def process_successful_payment(message: Message):
    stars_paid = message.successful_payment.total_amount
    await message.answer(f"Спасибо за донат! ✨ Вам зачислено {stars_paid} звёзд.")
