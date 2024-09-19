import asyncio
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
from user_states import UserStates
from keyboards import keyboards

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привет, я бот мониторинга новостей VK для сотрудников ЦОДД.")
    time.sleep(0.5)
    kb = keyboards[UserStates.BASE]
    await message.answer("Нажмите кнопку 'Поиск' и введите ключевые слова, что бы подобрать новости.", reply_markup=kb)
    await state.set_state(UserStates.BASE)
async def search(message: types.Message, state: FSMContext):
    if message.text == 'Поиск':
        markup = types.ReplyKeyboardRemove()
        kb = keyboards[UserStates.BASE]
        await message.answer("Теперь введите ключевые слова:",  markup=markup)
        messages = list()
        messages.append(message.text)
        await message.answer(f'{messages}', markup=kb)
    await state.set_state(UserStates.BASE)

# @dp.message(Command("Поиск"))
# async def search(message: types.Message, state: FSMContext):
#     await message.answer("Теперь введите ключевые слова:", reply_markup=None)
#     await state.set_state(UserStates.BASE)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot start was completed")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
