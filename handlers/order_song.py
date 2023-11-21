from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from admin.toggle_event_mode import get_reverted_state_of_event_mode, get_state_of_event_mode
from admin.toggle_order_songs_mode import get_reverted_state_of_order_songs_mode, get_state_of_order_songs_mode
from core.post_data_to_virtual_dj import post_data_to_virualdj
from filters.is_prof_bureau import IsProfBureau
from handlers import basic
from handlers.basic import menu
from utils.states import OrderSong

"""
Main functionality of bot, ordering a song
"""

router = Router()


@router.message(Command("song"), get_reverted_state_of_event_mode, lambda msg: ~IsProfBureau(msg))
@router.message(
    F.text.lower().in_(["🔒 заказать песню", "заказать песню 🎶", "заказать песню", "песня", "dj", "заказать"]),
    lambda msg: ~IsProfBureau(msg),
    get_reverted_state_of_event_mode)
@router.message(Command("song"), get_reverted_state_of_order_songs_mode, lambda msg: ~IsProfBureau(msg))
@router.message(
    F.text.lower().in_(["🔒 заказать песню", "заказать песню 🎶", "заказать песню", "песня", "dj", "заказать"]),
    get_reverted_state_of_order_songs_mode, lambda msg: ~IsProfBureau(msg))
async def songs_order_is_unavailable(message: Message):
    """
    If songs order is unavailable now, not include prof bureau and admin role
    :param message:
    """
    await message.answer("В данный момент нельзя заказать песню")
    await message.answer_sticker("CAACAgIAAxkBAAEKxaZlV88mmkmHF32kCRG4_vlq-vb-ugAClh8AAmytIUkmN-0qNzZa3zME")
    await menu(message)


# /song
@router.message(Command("song"), get_state_of_event_mode, get_state_of_order_songs_mode)
@router.message(Command("song"), IsProfBureau)
async def song_command(message: Message, state: FSMContext, command: CommandObject):
    """
    Order song command (/song)
    :param message: Message
    :param state: FSMContext
    :param command: CommandObject
    """
    # If /song has args
    if command.args is not None:
        return await send_song_go_menu(message, state, str(command.args))
    await song_text_command(message, state)


# Order song command
@router.message(
    F.text.lower().in_(["🔒 заказать песню", "заказать песню 🎶", "заказать песню", "песня", "dj", "заказать"]),
    get_state_of_event_mode, get_state_of_order_songs_mode)
@router.message(
    F.text.lower().in_(["🔒 заказать песню", "заказать песню 🎶", "заказать песню", "песня", "dj", "заказать"]),
    IsProfBureau)
async def song_text_command(message: Message, state: FSMContext):
    """
    Text song order command
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(OrderSong.song)
    await message.answer("✨ Хорошо!\n"
                         "Напиши автора и название песни\n"
                         "в условном формате:\n\n"
                         "✅ <code>Название песни - Автор песни</code>")


@router.message(OrderSong.song)
async def checking_song_name(message: Message, state: FSMContext):
    """
    Checking song name
    :param message: Message
    :param state: FSMContext
    """
    await state.update_data(song=message.text)
    data = await state.get_data()
    if isinstance(data["song"], str) and len(data["song"]) > 3:  # if song is text message and more 4 letters
        await send_song_go_menu(message, state, data)
    else:
        await send_song_again(message, state)


@router.message(OrderSong.song)
async def send_song_again(message: Message, state: FSMContext):
    """
    Request to enter again
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(OrderSong.song)
    await message.answer("Прости, но нужно написать песню в условном формате\n\n"
                         "✅ <code>Название песни - Автор песни</code>")


# Go back function, clear state and post
async def send_song_go_menu(message, state, data):
    """
    Call post_data_to_virualdj() with needed params
    :param message: Message
    :param state: FSMContext
    :param data: dict
    """
    if isinstance(data, dict):
        data = data["song"]
    await post_data_to_virualdj(
        f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} ID: "
        f"{message.from_user.id}",
        data)
    print(f'Заказана песня: "{data}", от пользователя: @{message.from_user.username} ID: {message.from_user.id}')
    await state.clear()
    await message.answer("Песня отправлена 💙")
    await message.answer_sticker("CAACAgIAAxkBAAEKw-xlViRRN89v0aRX4lqLAAE_8-WkTtwAAhAgAAJ4iilJz8JKJAMRcx8zBA")
    await basic.menu(message)
