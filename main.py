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

    pidor_fullname = message.reply_to_message.from_user.full_name

    buttonyes = InlineKeyboardButton("Да", callback_data='Yes.'+ pidor_fullname)
    buttonno = InlineKeyboardButton("Нет", callback_data='No')
    buttons = InlineKeyboardMarkup()
    buttons.add(buttonyes)
    buttons.add(buttonno)

    if message.reply_to_message == None:
        return  # Выход из функции, else не нужон

    await message.reply(f'Проголосовать за бан этого пидораса {pidor_fullname} ?', reply_markup=buttons)

    @dp.callback_query_handler(lambda c: 'Yes' in c.data)
    async def process_callback_buttonyes(callback_query: types.CallbackQuery):
        pidor_fullname = callback_query.data.split(".")[1]
        if process_callback_buttonyes == process_callback_buttonyes:
            await callback_query.message.edit_text(f'Проголосовать за бан этого пидораса {pidor_fullname} ? 1 человек проголосовал!', reply_markup=buttons)
            

















executor.start_polling(dp, skip_updates=True)
