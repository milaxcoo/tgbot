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
    item1 = types.InlineKeyboardButton("Котики", callback_data='cats')
    item2 = types.InlineKeyboardButton("Собачки", callback_data='dogs')
    item3 = types.InlineKeyboardButton("Город", callback_data='city')
    item4 = types.InlineKeyboardButton("Природа", callback_data='nature')
    item5 = types.InlineKeyboardButton("Автомобили", callback_data='cars')
    item6 = types.InlineKeyboardButton("Спорт", callback_data='sport')
    item7 = types.InlineKeyboardButton("Еда", callback_data='food')
    item8 = types.InlineKeyboardButton("Ночь", callback_data='night')
    item9 = types.InlineKeyboardButton("Техника", callback_data='tech')
    item10 = types.InlineKeyboardButton("Архитектура", callback_data='arch')
    
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'cats':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?cat,cats')
            elif call.data == 'dogs':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?dog,dogs')
            elif call.data == 'city':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?city')
            elif call.data == 'nature':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?nature')
            elif call.data == 'cars':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?car,cars')
            elif call.data == 'sport':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?sport')
            elif call.data == 'food':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?food')
            elif call.data == 'night':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?night')
            elif call.data == 'tech':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?tech')
            elif call.data == 'arch':
                bot.send_photo(call.message.chat.id, 'https://source.unsplash.com/random/?arch')
            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите категорию:", reply_markup=None)
            
            #show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Это тестовое уведомление!!11")
    except Exception as e:
        print(repr(e))

bot.infinity_polling()