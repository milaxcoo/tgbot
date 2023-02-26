import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе с поиском картинки.'.format(message.from_user, bot.get_me()), parse_mode='html')

#find image
@bot.message_handler(content_types=['text'])
def find_image(message):
    #keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Котики", callback_data='cat')
    item2 = types.InlineKeyboardButton("Собачки", callback_data='dog')
    item3 = types.InlineKeyboardButton("Люди", callback_data='people')
    item4 = types.InlineKeyboardButton("Природа", callback_data='nature')
    item5 = types.InlineKeyboardButton("Автомобили", callback_data='car')
    item6 = types.InlineKeyboardButton("Космос", callback_data='space')
    item7 = types.InlineKeyboardButton("Еда", callback_data='food')
    item8 = types.InlineKeyboardButton("Спорт", callback_data='sport')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id, 'Выбери категорию:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'cat':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'dog':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'people':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'nature':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'car':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'space':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'food':
                bot.send_message(call.message.chat.id, 'https://www.google.com')
            elif call.data == 'sport':
                bot.send_message(call.message.chat.id, 'https://www.google.com')

            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери категорию:", reply_markup=None)

            #show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Это тестовое уведомление!!11")

    except Exception as e:
        print(repr(e))

        

bot.infinity_polling()