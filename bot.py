import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord

API_TOKEN = '5622995349:AAFwQnNKd-_iG2IMALD45AqE0lb18cwn5wA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("O'zbek Imlo Botiga Xush Kelibsiz!")


@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text.split()
    for i in word:
            result = checkWord(i)

            if result['avialable']:
                response=f'✅ {i.capitalize()}'

            else:
                response=f'❌ {i.capitalize()}\n'
                for text in result['matches']:
                    response+=f'✅ {text.capitalize()}\n'


            await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)