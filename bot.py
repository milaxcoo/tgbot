import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, "Sup, bro?")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()