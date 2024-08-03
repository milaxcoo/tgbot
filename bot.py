from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.reply("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_messages(message):
    print('Мы получили сообщение')
    await message.reply(message.text.upper())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)