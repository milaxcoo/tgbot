import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе с поиском картинки.'.format(message.from_user, bot.get_me()), parse_mode='html')

#find image from internet
@bot.message_handler(commands=['findpic'])
def findpic(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Котики", callback_data='cat')
    item2 = types.InlineKeyboardButton("Собачки", callback_data='dog')
    item3 = types.InlineKeyboardButton("Люди", callback_data='people')
    item4 = types.InlineKeyboardButton("Природа", callback_data='nature')
    item5 = types.InlineKeyboardButton("Автомобили", callback_data='cars')
    item6 = types.InlineKeyboardButton("Спорт", callback_data='sport')
    item7 = types.InlineKeyboardButton("Еда", callback_data='food')
    item8 = types.InlineKeyboardButton("Природа", callback_data='nature')
    item9 = types.InlineKeyboardButton("Техника", callback_data='tech')
    item10 = types.InlineKeyboardButton("Архитектура", callback_data='arch')
    item11 = types.InlineKeyboardButton("Животные", callback_data='animals')
    item12 = types.InlineKeyboardButton("Разное", callback_data='other')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
    bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'cat':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/category/cats')
            elif call.data == 'dog':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/category/dogs')


    except Exception as e:
        print(repr(e))
        
bot.infinity_polling()