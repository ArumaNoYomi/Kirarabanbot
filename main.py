from config import BOT_API
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

database = {}

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
    # await callback_query.message.edit_text(f'Проголосовать за бан этого пидораса {pidor_fullname} ? 1 человек проголосовал!', reply_markup=buttons)
    if (callback_query.message.chat.id, callback_query.message.message_id) in database:
        database[(callback_query.message.chat.id, callback_query.message.message_id)].add(callback_query.from_user.id)
    else:
        database[(callback_query.message.chat.id, callback_query.message.message_id)] = set([callback_query.from_user.id])
    await callback_query.answer()
    for key in database:
        counter = (len(database[key]))
#        if counter == 7:
#           await
