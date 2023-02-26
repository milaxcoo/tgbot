import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который умеет считать слова в тексте. Отправь мне текст, а я посчитаю слова в нем.')

bot.polling(none_stop=True)