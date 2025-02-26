import asyncio
import os


from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello This is your first bot!!!')

@dp.message(Command("info"))
async def info(message: types.Message):
    await message.answer("This bot can talk with you")

@dp.message(Command('Sabina'))
async def Sabina(message: types.Message):
    await  message.reply('Assistent')
@dp.message()
async def echo(message: types.Message):
    if message.sticker:
            await message.answer(f"{message.sticker.file_id}")
    elif message.text == 'Aidin' or message.text == 'Aman':
        await message.answer_sticker('CAACAgIAAxkBAAMdZ774lbXrQbMjHK-fjmlQjVzMnLsAAvokAAIzwXlIhTeUtDWQgyw2BA')
        await message.answer_sticker('CAACAgIAAxkBAAMoZ776Q4xQJWH8_Qqmz16EtcdMyhgAAnNdAAJeimhIQ__VqJID5r42BA')
        await message.answer_sticker('CAACAgIAAxkBAAMqZ776RMoaMVop9qbhtoBVj8HN9RoAAr9hAAI9RGhIULmp0_372no2BA')
async  def main():
    print('Bot started...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

