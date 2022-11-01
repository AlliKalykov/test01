import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message.chat.id, "I'm a bot, please talk to me!")
