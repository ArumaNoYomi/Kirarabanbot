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


    pidor_fullname = message.reply_to_message.from_user.full_name
    pidorid = message.reply_to_message.from_user.id

    buttonyes = InlineKeyboardButton("Да", callback_data='Yes.'+ pidor_fullname +"."+ str(pidorid))
    buttonno = InlineKeyboardButton("Нет", callback_data='No')
    buttons = InlineKeyboardMarkup()
    buttons.add(buttonyes)
    buttons.add(buttonno)

    if message.reply_to_message == None:
        return  # Выход из функции, else не нужон

    await message.reply(f'Проголосовать за бан этого пидораса {pidor_fullname} ?', reply_markup=buttons)
    with open("golosovanie.opus", mode="rb") as file:
        binary_content = file.read()
    await message.reply_voice(binary_content, reply=False)

@dp.callback_query_handler(lambda c: 'Yes' in c.data)
async def process_callback_buttonyes(callback_query: types.CallbackQuery):
    pidor_fullname = callback_query.data.split(".")[1]


    pidorid = int(callback_query.data.split(".")[2])
    key = callback_query.message.chat.id, callback_query.message.message_id

    if (key) in database:
        database[(key)].add(callback_query.from_user.id)
    else:
        database[(key)] = set([callback_query.from_user.id])
    await callback_query.answer()

    buttonyes = InlineKeyboardButton("Да", callback_data='Yes.' + pidor_fullname + "." + str(pidorid))
    buttonno = InlineKeyboardButton("Нет", callback_data='No')
    buttons = InlineKeyboardMarkup()
    buttons.add(buttonyes)
    buttons.add(buttonno)

    for key in database:
        counter = len(database[key])
        if counter == 10:
            await bot.ban_chat_member(callback_query.message.chat.id, pidorid)
            await callback_query.message.edit_text(f'Проголосовать за бан этого пидораса {pidor_fullname} ? Пидор забанен!', reply_markup=buttons)
        else:
            try:
                await callback_query.message.edit_text(f'Проголосовать за бан этого пидораса {pidor_fullname} ? {counter}', reply_markup=buttons)
            except Exception as e:
                pass

executor.start_polling(dp, skip_updates=True)
