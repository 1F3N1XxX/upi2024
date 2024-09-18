import asyncio
import random
import types

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from user_states import UserStates
from keyboard import keyboards

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет, я бот мониторинга новостей VK для сотрудников ЦОДД", reply_markup=kb)
    await state.set_state(UserStates.BASE)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot start was completed")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
