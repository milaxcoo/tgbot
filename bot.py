import telebot
import config
import requests

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nI am - <b>{1.first_name}</b>, the bot created to find pics fo u!'.format(message.from_user, bot.get_me()), parse_mode='html')

    #keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = telebot.types.KeyboardButton("🎲 Random")
    item2 = telebot.types.KeyboardButton("🐈‍⬛ Cats")
    item3 = telebot.types.KeyboardButton("🐕 Dogs")
    item4 = telebot.types.KeyboardButton("🌹 Nature")
    item5 = telebot.types.KeyboardButton("🍔 Food")
    item6 = telebot.types.KeyboardButton("🚗 Cars")
    item7 = telebot.types.KeyboardButton("🔎 Search")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, 'Choose the type below ↓', reply_markup=markup)

#get image by keyboard
@bot.message_handler(content_types=['text'])
def get_image(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Random':
            r = requests.get('https://source.unsplash.com/random', timeout=5)
            url = r.url
            #inline keyboard
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)
            
        elif message.text == '🐈‍⬛ Cats':
            r = requests.get('https://source.unsplash.com/random/?cats', timeout=5)
            url = r.url
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)

        elif message.text == '🐕 Dogs':
            r = requests.get('https://source.unsplash.com/random/?dogs', timeout=5)
            url = r.url
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)
            
        elif message.text == '🌹 Nature':
            r = requests.get('https://source.unsplash.com/random/?nature', timeout=5)
            url = r.url
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)
            
        elif message.text == '🍔 Food':
            r = requests.get('https://source.unsplash.com/random/?food', timeout=5)
            url = r.url
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)
           
        elif message.text == '🚗 Cars':
            r = requests.get('https://source.unsplash.com/random/?cars', timeout=5)
            url = r.url
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)
            
        elif message.text == '🔎 Search':
            bot.send_message(message.chat.id, 'What we\'re searching for?')
            bot.register_next_step_handler(message, get_keyword)
        else:
            bot.send_message(message.chat.id, 'I don\'t understand you. Please, choose one letter from the keyboard.')

def get_keyword(message):
    r = requests.get('https://source.unsplash.com/random/?{0}'.format(message.text), timeout=5)
    url = r.url
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    item1 = telebot.types.InlineKeyboardButton("👍", callback_data='like')
    item2 = telebot.types.InlineKeyboardButton("👎", callback_data='dislike')
    markup.add(item1, item2)
    bot.send_photo(message.chat.id, url, reply_markup=markup)
    
#like/dislike
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'like':
                bot.send_message(call.message.chat.id, '☺️')
            elif call.data == 'dislike':
                bot.send_message(call.message.chat.id, '🧐')
            #remove inline buttons from message
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
            #show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="This is test alert")
    except Exception as e:
        print(repr(e))

bot.infinity_polling()