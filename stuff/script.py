import telebot 
from telebot import types

bot = telebot.TeleBot('1081649953:AAHL0QhldENzi-FACVVlNOhDMnEGLWR71Q0') 
STICKER = 'CAACAgIAAxkBAAL3tl7yLjSE9G1Uo9W9hZQ8BonLFjpkAAIFAAPANk8T-WpfmoJrTXUaBA'

#Welcome or just /start 
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, STICKER)
    bot.send_message(message.chat.id,'Hi ⚜️{0}⚜️!\nGlad to see you!😊'.format(message.from_user.first_name))
    bot.send_message(message.chat.id,'If you want to understand for what I have created this bot,type✍ /help!')
    bot.send_message(message.chat.id,'If you want to start to use the feautures of the bot, type✍ /keyboard')

#Keyboard
@bot.message_handler(commands=['keyboard'])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup()
    button_ds_sources = types.KeyboardButton('DS Sources📚')
    button_awesome_data = types.KeyboardButton('Awesome data github👑')
    button_ds_practice = types.KeyboardButton('Practice 💪')
    button_ds_path = types.KeyboardButton('Data Science Advices💻')
    button_gay = types.KeyboardButton('Gay')
    #Here I set the place of the buttonse
    markup.row(button_awesome_data,button_ds_practice)
    markup.row(button_ds_sources,button_ds_path,button_gay)
    bot.send_message(message.chat.id,'Your main menu:',reply_markup=markup)

@bot.message_handler(content_types=['text'])#Am facut 
def response(message):
    if message.chat.type == 'private':
        if message.text == 'DS Sources📚':
            bot.send_message(message.chat.id, 'l')
        if message.text == 'Data Science Advices💻':
            bot.send_message(message.chat.id, 'l')
        if message.text == 'Practice 💪':
            bot.send_message(message.chat.id , 'l')
        if message.text == 'Awesome data github👑':
            bot.send_message(message.chat.id , 'l')
        if message.text == 'Gay':
            bot.send_message(message.chat.id, 'Sobolan')

#About bot and about 
@bot.message_handler(commands=['aboutus'])
def about_us(message):
    pass
    
bot.polling()