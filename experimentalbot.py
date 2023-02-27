import telebot
import config
import requests


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nI am - <b>{1.first_name}</b>, the bot created to find pics fo u!'.format(message.from_user, bot.get_me()), parse_mode='html')

    #keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Random pic")
    item2 = telebot.types.KeyboardButton("Cats")
    item3 = telebot.types.KeyboardButton("Dogs")
    item4 = telebot.types.KeyboardButton("Nature")
    item5 = telebot.types.KeyboardButton("Food")
    item6 = telebot.types.KeyboardButton("Cars")
    item7 = telebot.types.KeyboardButton("Own keyword")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, 'Choose one letter:', reply_markup=markup)


#get image by keyboard
@bot.message_handler(content_types=['text'])
def get_image(message):
    if message.chat.type == 'private':
        if message.text == 'Random pic':
            r = requests.get('https://source.unsplash.com/random', timeout=5)
            url = r.url
            #inline keyboard
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("Like", callback_data='like')
            item2 = telebot.types.InlineKeyboardButton("Dislike", callback_data='dislike')
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, url, reply_markup=markup)
            

        elif message.text == 'Cats':
            r = requests.get('https://source.unsplash.com/random/?cats', timeout=5)
            url = r.url
            bot.send_photo(message.chat.id, url)

        elif message.text == 'Dogs':
            r = requests.get('https://source.unsplash.com/random/?dogs', timeout=5)
            url = r.url
            bot.send_photo(message.chat.id, url)
            
        elif message.text == 'Nature':
            r = requests.get('https://source.unsplash.com/random/?nature', timeout=5)
            url = r.url
            bot.send_photo(message.chat.id, url)
            
        elif message.text == 'Food':
            r = requests.get('https://source.unsplash.com/random/?food', timeout=5)
            url = r.url
            bot.send_photo(message.chat.id, url)
           
        elif message.text == 'Cars':
            r = requests.get('https://source.unsplash.com/random/?cars', timeout=5)
            url = r.url
            bot.send_photo(message.chat.id, url)
            
        elif message.text == 'Own keyword':
            bot.send_message(message.chat.id, 'Type your keyword:')
            bot.register_next_step_handler(message, get_keyword)
        else:
            bot.send_message(message.chat.id, 'I don\'t understand you. Please, choose one letter from the keyboard.')


def get_keyword(message):
    r = requests.get('https://source.unsplash.com/random/?{0}'.format(message.text), timeout=5)
    url = r.url
    bot.send_photo(message.chat.id, url)
    
#like/dislike
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'like':
                bot.send_message(call.message.chat.id, 'Thank you for your feedback!')
            elif call.data == 'dislike':
                bot.send_message(call.message.chat.id, 'Thank you for your feedback!')
            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Choose one letter:", reply_markup=None)
            #show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="This is test alert")
    except Exception as e:
        print(repr(e))
        
bot.infinity_polling()