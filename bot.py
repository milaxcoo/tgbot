import telebot
import config
import requests


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    #welcome
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nI am - <b>{1.first_name}</b>, the bot created to find pics fo u!\nJust type only one keyword!'.format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def image(message):
    r = requests.get('https://source.unsplash.com/random/?{0}'.format(message.text), timeout=5)
    url = r.url
    bot.send_photo(message.chat.id, url)


bot.infinity_polling()