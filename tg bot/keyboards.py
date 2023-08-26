from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

ikb_categories = InlineKeyboardMarkup(row_width = 1)
ib1 = InlineKeyboardButton(text = "в коробке", callback_data = "5")
ib2 = InlineKeyboardButton(text = "в одежде", callback_data = "15")
ib3 = InlineKeyboardButton(text = "с головным убором", callback_data = "1")
ib4 = InlineKeyboardButton(text = "в раковине🤨", callback_data = "14")
ib5 = InlineKeyboardButton(text = "в космосе", callback_data = "2")
ib6 = InlineKeyboardButton(text = "в очках", callback_data = "4")
ib7 = InlineKeyboardButton(text = "с галстуком", callback_data = "7")
ikb_categories.add(ib1).add(ib2).add(ib3).add(ib4).add(ib5).add(ib6).add(ib7)

kb = ReplyKeyboardMarkup(resize_keyboard = True)
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/categories')
kb.add(b2).add(b3)

ikb_evaluation = InlineKeyboardMarkup(row_width = 2)
ib8 = InlineKeyboardButton(text = "❤️", callback_data = "like")
ib9 = InlineKeyboardButton(text = "👎🏻", callback_data = "dislike")
ib10 = InlineKeyboardButton(text = "Выбрать категорию", callback_data = "categories")
ikb_evaluation.add(ib8, ib9).add(ib10)