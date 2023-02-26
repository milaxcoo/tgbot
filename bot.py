import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nI am - <b>{1.first_name}</b>, the bot created to find pics fo u.'.format(message.from_user, bot.get_me()), parse_mode='html')



#find random image for each request
@bot.message_handler(content_types=['text'])
def send_image(message):
    if message.chat.type == 'private':
        if message.text == 'cat':
            bot.send_photo(message.chat.id, open('cat.jpg', 'rb'))
        elif message.text == 'dog':
            bot.send_photo(message.chat.id, open('dog.jpg', 'rb'))
        else:
            bot.send_message(message.chat.id, 'I don\'t understand you.')



bot.infinity_polling()