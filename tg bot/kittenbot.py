from aiogram import Bot, Dispatcher, executor, types
from keyboards import kb, ikb_categories, ikb_evaluation 
from config import BOT_TOKEN
from request import get_photo 


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/categories</b> - <em>категории фото</em>  
"""
@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await message.answer(text = "Привет! Я отправляю котиков по твоему запросу, выбери категорию и наслаждайся.",
                         reply_markup = kb)
    await message.delete()

@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await message.answer(text = HELP_COMMAND,
                         parse_mode = 'HTML')
    await message.delete()
          
     
@dp.message_handler(commands = ['categories'])
async def categories_command(message: types.Message):
    await message.answer(text = 'Выберите категорию:', 
                         reply_markup = ikb_categories)
    await message.delete()

@dp.callback_query_handler(lambda callback: callback.data in ["like", "dislike", "categories",])
async def callback_evaluation(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer("Тебе понравилось🥳!")
    elif callback.data == "dislike":
        await callback.answer("Тебе не понравилось😔")
    elif callback.data == "categories":
        await callback.message.answer("Выберите категорию:", 
                         reply_markup = ikb_categories)
    else:
        await callback.answer()

@dp.callback_query_handler(lambda callback: int(callback.data) in [5, 15, 1, 14, 2, 4, 7])
async def callback_photo(callback: types.CallbackQuery):      
    category = callback.data
    result = get_photo(category) 
    data = (result.json())
    photo = data[0]
    url = photo.get("url")
    await bot.send_photo(chat_id = callback.message.chat.id,
                         photo = url,
                         reply_markup = ikb_evaluation)
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

