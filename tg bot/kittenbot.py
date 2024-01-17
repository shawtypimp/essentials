import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from keyboards import kb_commands, builder_categories, builder_evaluation 
from config import BOT_TOKEN
from request import get_photo 


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/categories</b> - <em>категории фото</em>  
"""
@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(text = "Привет! Я отправляю котиков по твоему запросу, выбери категорию и наслаждайся.",
                         reply_markup = kb_commands)
    await message.delete()

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer(text = HELP_COMMAND,
                         parse_mode = 'HTML')
    await message.delete()
          
     
@dp.message(Command('categories'))
async def categories_command(message: types.Message):
    await message.answer(text = 'Выберите категорию:', 
                         reply_markup = builder_categories.as_markup())
    await message.delete()

@dp.callback_query(lambda callback: callback.data in ["like", "dislike", "categories",])
async def callback_evaluation(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer("Тебе понравилось🥳!")
    elif callback.data == "dislike":
        await callback.answer("Тебе не понравилось😔")
    elif callback.data == "categories":
        await callback.message.answer("Выберите категорию:", 
                         reply_markup = builder_categories.as_markup())
    else:
        await callback.answer()

@dp.callback_query(lambda callback: int(callback.data) in [5, 15, 1, 14, 2, 4, 7])
async def callback_photo(callback: types.CallbackQuery):      
    category = callback.data
    result = get_photo(category) 
    data = (result.json())
    photo = data[0]
    url = photo.get("url")
    await bot.send_photo(chat_id = callback.message.chat.id,
                         photo = url,
                         reply_markup = builder_evaluation.as_markup())
        
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

