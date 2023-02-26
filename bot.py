import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')

if __name__ == '__main__':
    bot.polling(none_stop=True)