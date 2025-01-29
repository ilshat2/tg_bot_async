from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from dotenv import load_dotenv
import logging
import asyncio
import os


logging.basicConfig(level=logging.INFO)

load_dotenv()  # Загружаем переменные из .env


TELEGRAM_TOKEN = os.getenv('MY_TELEGRAM_TOKEN')

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()  # Создаем экземпляр хранилища

# Инициализация диспетчера с указанием хранилища
dp = Dispatcher(storage=storage)  # Передаем через ключевые параметры
#dp = Dispatcher(bot)

# Создаем роутер
#router = dp.router

# Инициализация диспетчера с правильной передачей bot через параметр bot
#dp = Dispatcher()

# Добавляем bot в dispatcher через метод setup
#dp.include_router(bot)

# Инициализация диспетчера
#dp = Dispatcher(bot)


# Обработчик для команды /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!")


# Обработчик для всех сообщений
@dp.message()
async def echo(message: Message):
    # Здесь текст, который будет отвечать бот
    await message.answer(f"Ты сказал: {message.text}")


async def main():
    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Запуск асинхронной функции main
    asyncio.run(main())
