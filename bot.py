import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, "Sup, bro?")

bot.polling()
#bot.infinity_polling()