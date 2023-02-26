import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nI am - <b>{1.first_name}</b>, the bot created to find pics fo u.'.format(message.from_user, bot.get_me()), parse_mode='html')



#find random image for every message
@bot.message_handler(content_types=['text'])
def send_image(message):
    bot.send_photo(message.chat.id, 'https://picsum.photos/200/300/?random')


bot.infinity_polling()