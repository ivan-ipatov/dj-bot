from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from admin.toggle_order_songs_mode import get_state_of_order_songs_mode, toggle_order_songs_mode
from filters.is_admin import IsAdmin
from handlers import basic
from keyboards.builder_keyboard import build_kb, rmk
from utils.states import RequestForToggleOrderSongsMode

"""
Only admin command
Toggle order songs mode from bot 
"""
router = Router()


# /ToggleOrderSongsMode or Turn on/off songs
@router.message(IsAdmin(), Command("ToggleOrderSongsMode"))
@router.message(IsAdmin(), F.text.lower().in_(["⛔ выключить песни", "✅ включить песни"]))
async def get_request(message: Message, state: FSMContext):
    """
    Alert with keyboard about toggle order songs mode
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(RequestForToggleOrderSongsMode.confirm)
    if get_state_of_order_songs_mode() is True:
        await message.answer("❗ Вы действительно хотите выключить режим заказа песен?",
                             reply_markup=build_kb(["Да", "Отмена"]))
    else:
        await message.answer("❗ Вы действительно хотите включить режим заказа песен?",
                             reply_markup=build_kb(["Да", "Отмена"]))


@router.message(RequestForToggleOrderSongsMode.confirm)
async def send_result(message: Message, state: FSMContext):
    """
    Toggle order songs mode and send result to admin
    :param message: Message
    :param state: FSMContext
    """
    await state.update_data(confirm=message.text)
    data = await state.get_data()
    await state.clear()
    if str(data["confirm"]) == "Да":
        toggle_order_songs_mode()
        if get_state_of_order_songs_mode() is True:
            print(f"Админ: @{message.from_user_username} запустил режим заказа песен")
            await message.answer("✅ Режим заказа песен успешно включён", reply_markup=rmk)
        else:
            print(f"Админ: @{message.from_user_username} выключил режим заказа песен")
            await message.answer("❌ Режим заказа песен успешно выключен", reply_markup=rmk)
    await basic.menu(message)
