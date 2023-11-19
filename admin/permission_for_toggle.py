from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db
from admin.toggle_func import do_toggle, get_toggle_true
from filters.is_admin import IsAdmin
from handlers import basic
from keyboards.builder_keyboard import builder_kb, rmk
from utils.states import PermissionOrder

router = Router()

@router.message(IsAdmin(), Command("ChangeEventMode"))
@router.message(IsAdmin(), F.text.lower().in_(["⛔ выключить меро", "✅ включить "
                                                                   "мероприятие"]))
async def get_permission(message: Message, state: FSMContext):
    await state.set_state(PermissionOrder.perm)
    if get_toggle_true() is True:
        await message.answer("❗ Вы действительно хотите выключить режим мероприятия?",
                             reply_markup=builder_kb(["Да", "Отмена"]))
    else:
        await message.answer("❗ Вы действительно хотите включить режим мероприятия?",
                             reply_markup=builder_kb(["Да", "Отмена"]))


@router.message(PermissionOrder.perm)
async def order_song(message: Message, state: FSMContext):
    await state.update_data(perm=message.text)
    data = await state.get_data()
    await state.clear()
    if str(data["perm"]) == "Да":
        do_toggle()
        if get_toggle_true() is True:
            db.reference('likes').set(0)
            await message.answer("✅ Режим мероприятия успешно включён", reply_markup=rmk)
        else:
            await message.answer("❌ Режим мероприятия успешно выключен", reply_markup=rmk)
    await basic.menu(message)
