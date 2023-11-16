from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers import basic
from core.virtual_dj import send_song
from utils.states import OrderSongList


router = Router()


# /song, asking for song
@router.message(Command("song"))
async def set_song_command(message: Message, state: FSMContext, command: CommandObject):
    # If /song has args
    if command.args is not None:
        return await send_song_go_menu(message, state, str(command.args))
    await set_song_message(message, state)


# Order song message
@router.message(F.text.lower().in_(["заказать песню 🎶", "заказать песню", "песня", "dj", "заказать"]))
async def set_song_message(message: Message, state: FSMContext):
    await state.set_state(OrderSongList.song)
    await message.answer("✨ Хорошо!\n"
                         "Напиши автора и название песни\n"
                         "в условном формате:\n\n"
                         "✅ <code>Название песни - Автор песни</code>")


# post data to server
@router.message(OrderSongList.song)
async def order_song(message: Message, state: FSMContext):
    await state.update_data(song=message.text)
    data = await state.get_data()
    if isinstance(data["song"], str) and len(data["song"]) < 4: # if song is text message and more 4 letters
        await send_song_go_menu(message, state, data)
    else:
        await set_song_again(message, state)



# Request to enter again
@router.message(OrderSongList.song)
async def set_song_again(message: Message, state: FSMContext):
    await state.set_state(OrderSongList.song)
    await message.answer("Прости, но нужно написать песню в условном формате\n\n"
                         "✅ <code>Название песни - Автор песни</code>")


# Go back function, clear state and post
async def send_song_go_menu(message, state, data):
    if isinstance(data, dict): data = data["song"]
    await send_song(f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}",
                    data)
    await state.clear()
    await message.answer("Песня отправлена 💙")
    await message.answer_sticker("CAACAgIAAxkBAAEKw-xlViRRN89v0aRX4lqLAAE_8-WkTtwAAhAgAAJ4iilJz8JKJAMRcx8zBA")
    await basic.menu(message)