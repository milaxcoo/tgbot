import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе с поиском картинки.'.format(message.from_user, bot.get_me()), parse_mode='html')


#find image from google by keyword
@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_photo(message.chat.id, 'https://source.unsplash.com/random/?{0}'.format(message.text))



bot.infinity_polling()