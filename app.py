from aiogram import Bot, Dispatcher, types

# Создаем переменные бота где Bot(token='Токен нашего бота')
bot = Bot(token='Токен нашего бота')

# Создаем дмспетчер
dp = Dispatcher(bot)


@dp.message_handler()  # Все сообщения
async def get_message(message: types.Message):
    # Если в скобках написано (message: types.Message) то в скрипте мы можем использовать message вместо types.Message
    # Например получим айди пользователя:
    chat_id = types.Message.chad.id  # - первый вариант
    chat_id = message.chat.id  # второй вариант
    # При этом функуионал никак не изменился

    # Отправляем сообщение пользователю
    # Вариант 1
    chat_id = message.chat.id
    text = 'Текст которым отвечает бот'

    await bot.send_message(chat_id=chat_id, text=text)
