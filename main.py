import logging
from aiogram import Bot, Dispatcher, executor, types

from HolidaysInfo import messageEdit

API_TOKEN = '1996443920:AAGINBO_YWNK4Wr7Vd0dThFvQ3KJiri5zZ8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Assalomu alaykum.\n@uzholidays_bot ga xush kelibsiz!\n" 
    "Botdan foydalanish uchun yordam  /help")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Botdan foydalanish uchun biror bir davlat kodini yoki nomini jo'nating"
    " va bot sizga shu davlatda bugun qanaqa bayramlar borligi haqida ma'lumot beradi.\n"
    "Namuna:\nDavlat nomi 🙌🏿 O'zbekiston\nDavlat kodi 🙌🏿 UZ\n")

@dp.message_handler()
async def HolidaysInfo(message: types.Message):
    response = messageEdit(message.text)
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)