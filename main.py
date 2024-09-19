import asyncio
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from api_key import vk_key
from api import search_vk_posts, unix_to_date, sigmund

from config import TOKEN
from user_states import UserStates

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.reply("Привет, я бот мониторинга новостей VK для сотрудников ЦОДД.")
    time.sleep(0.5)
    await message.answer("Вводите ключевые слова, что бы подобрать новости.")
    await state.set_state(UserStates.BASE)


@dp.message(F.text.lower() != '', StateFilter(UserStates.BASE))
async def search(message: types.Message, state: FSMContext):
    a = message.text
    keywords = a.split()
    await message.answer(f'Результат поска по запросу: "{a}"')
    post_ = search_vk_posts(vk_key, keywords, address="Москва")
    for i in range(0, sigmund):
        await message.answer(f'Дата поста: {unix_to_date(post_[i][0])}\n\n{post_[i][1][:4000]}\n\nСсыка на пост: {post_[i][2]}')
        time.sleep(2)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot start was completed")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
