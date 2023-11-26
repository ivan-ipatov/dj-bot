from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db

from admin.toggle_event_mode import toggle_event_mode, get_state_of_event_mode
from filters.is_admin import IsAdmin
from handlers import basic
from keyboards.builder_keyboard import build_kb, rmk
from utils.states import RequestForToggleEventMode

"""
Only admin command
Toggle event mode from bot 
"""
router = Router()


# /ToggleEventMode or Turn on/off event
@router.message(IsAdmin(), Command("ToggleEventMode"))
@router.message(IsAdmin(), F.text.lower().in_(["⛔ выключить меро", "✅ включить "
                                                                   "мероприятие"]))
async def get_request(message: Message, state: FSMContext):
    """
    Alert with keyboard about toggle event mode
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(RequestForToggleEventMode.confirm)
    if get_state_of_event_mode() is True:
        await message.answer("❗ Вы действительно хотите выключить режим мероприятия?",
                             reply_markup=build_kb(["Да", "Отмена"]))
    else:
        await message.answer("❗ Вы действительно хотите включить режим мероприятия?",
                             reply_markup=build_kb(["Да", "Отмена"]))


@router.message(RequestForToggleEventMode.confirm)
async def send_result(message: Message, state: FSMContext):
    """
    Toggle event mode and send result to admin
    :param message: Message
    :param state: FSMContext
    """
    await state.update_data(confirm=message.text)
    data = await state.get_data()
    await state.clear()
    if str(data["confirm"]) == "Да":
        toggle_event_mode()
        if get_state_of_event_mode() is True:
            db.reference('likes').set(0)
            print(f"Админ: @{message.from_user.username} запустил режим мероприятия")
            await message.answer("✅ Режим мероприятия успешно включён", reply_markup=rmk)
        else:
            print(f"Админ: @{message.from_user.username} выключил режим мероприятия")
            await message.answer("❌ Режим мероприятия успешно выключен", reply_markup=rmk)
    await basic.menu(message)
