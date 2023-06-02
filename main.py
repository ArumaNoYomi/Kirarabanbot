from config import BOT_API
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=BOT_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def check(message: types.Message):
    if message.text == "/start":
        await message.reply("Hi!\nI'm Kirara!")

@dp.message_handler(commands=["voteban"])
async def check2(message: types.Message):

    await message.reply("Голосование") # добавить войсом голосование мем

    buttonyes = InlineKeyboardButton("Да", callback_data='Yes')
    buttonno = InlineKeyboardButton("Нет", callback_data='No')
    buttons = InlineKeyboardMarkup()
    buttons.add(buttonyes)
    buttons.add(buttonno)

    if message.reply_to_message == None:
        return  # Выход из функции, else не нужон

    pidor_id = message.reply_to_message.from_id
    pidor_fullname = message.reply_to_message.from_user.full_name
    await message.reply(f'Проголосовать за бан этого пидораса {pidor_fullname} ?', reply_markup=buttons)\

@dp.callback_query_handler(lambda c: c.data == 'buttonyes')
async def process_callback_buttonyes(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Проголосовать за бан этого пидораса {pidor_fullname} ? 1 человек проголосовал!')


















executor.start_polling(dp, skip_updates=True)
