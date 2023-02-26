import telebot
import config
import requests


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nI am - <b>{1.first_name}</b>, the bot created to find pics fo u.'.format(message.from_user, bot.get_me()), parse_mode='html')

#get random image
@bot.message_handler(commands=['get'])
def get(message):
    r = requests.get('https://aws.random.cat/meow')
    url = r.json()['file']
    bot.send_photo(message.chat.id, url)



bot.infinity_polling()