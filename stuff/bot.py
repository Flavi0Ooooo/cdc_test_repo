import telebot

bot = telebot.TeleBot("1246913420:AAHaR-dI_Iz-n4LX8FwcncdIPI5ejyX4GPU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()