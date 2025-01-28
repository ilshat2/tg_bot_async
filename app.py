from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Создаем переменные бота где Bot(token='Токен нашего бота')
bot = Bot(token='Токен нашего бота')

# Создаем дмспетчер
dp = Dispatcher(bot)


@dp.message_handler()  # Все сообщения
async def get_message(message: types.Message):
    # Если в скобках написано (message: types.Message) то в скрипте мы можем использовать message вместо types.Message
    # Например получим айди пользователя:
    #chat_id = types.Message.chad.id  # - первый вариант
    #chat_id = message.chat.id  # второй вариант
    # При этом функуионал никак не изменился

    # Отправляем сообщение пользователю

    # Вариант 1
    text = f'Привет {message.from_user.full_name}'
    await message.answer(text=text)

    print(message.text)


    # Вариант 2
    #chat_id = message.chat.id
    #text = 'Текст которым отвечает бот'
    #await bot.send_message(chat_id=chat_id, text=text)

    # Вариант 3
    #text = 'Текст ответа для варианта 2'
    #await message.answer(text=text)

    # Вариант 4 (Ответ текстом который отправил пользователь)
    #text = message.text
    #await message.answer(text=text)


executor.start_polling(dp)
