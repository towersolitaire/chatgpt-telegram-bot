import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6155381091:AAFPcgCkC72Jwl_zmdGyq6b-ZoUGsre_O0Q'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_command(message : types.Message):
    await message.answer("123")


@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
    )
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)