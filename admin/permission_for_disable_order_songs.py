import os

from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from admin.order_toggle_func import get_toggle_true_order, do_toggle_order
from filters.is_admin import IsAdmin
from handlers import basic
from keyboards.builder_keyboard import builder_kb, rmk
from utils.states import Permission

router = Router()


@router.message(IsAdmin(), Command("ChangeSongOrderMode"))
@router.message(IsAdmin(), F.text.lower().in_(["⛔ выключить песни", "✅ включить песни"]))
async def get_permission(message: Message, state: FSMContext):
    await state.set_state(Permission.perm)
    if get_toggle_true_order() is True:
        await message.answer("❗ Вы действительно хотите выключить режим заказа песен?", reply_markup=builder_kb(["Да", "Отмена"]))
    else:
        await message.answer("❗ Вы действительно хотите включить режим заказа песен?", reply_markup=builder_kb(["Да", "Отмена"]))


@router.message(Permission.perm)
async def order_song(message: Message, state: FSMContext):
    await state.update_data(perm=message.text)
    data = await state.get_data()
    await state.clear()
    if str(data["perm"]) == "Да":
        do_toggle_order()
        if get_toggle_true_order() is True:
            await message.answer("✅ Режим заказа песен успешно включён", reply_markup=rmk)
        else:
            await message.answer("❌ Режим заказа песен успешно выключен", reply_markup=rmk)
    await basic.menu(message)
