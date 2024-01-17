from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



builder_categories = InlineKeyboardBuilder()
builder_categories.row(
    types.InlineKeyboardButton(text = "в коробке", callback_data = "5"),
    types.InlineKeyboardButton(text = "в одежде", callback_data = "15"),
    types.InlineKeyboardButton(text = "с головным убором", callback_data = "1"),
    types.InlineKeyboardButton(text = "в раковине🤨", callback_data = "14"),
    types.InlineKeyboardButton(text = "в космосе", callback_data = "2"),
    types.InlineKeyboardButton(text = "в очках", callback_data = "4"),
    types.InlineKeyboardButton(text = "с галстуком", callback_data = "7"),
    width = 1
)

kb_commands = ReplyKeyboardMarkup(keyboard = [
        [
            KeyboardButton(text = '/help'),
            KeyboardButton(text = '/categories'),
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True)

builder_evaluation = InlineKeyboardBuilder()
builder_evaluation.row(
    types.InlineKeyboardButton(text = "❤️", callback_data = "like"),
    types.InlineKeyboardButton(text = "👎🏻", callback_data = "dislike"),
    types.InlineKeyboardButton(text = "Выбрать категорию", callback_data = "categories"),
    width = 2
)
