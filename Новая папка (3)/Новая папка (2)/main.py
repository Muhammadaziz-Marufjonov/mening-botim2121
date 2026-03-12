import telebot

TOKEN = "8550247332:AAHtBSV2zIQZT_swY0CnKYw_IcDqL0bLc8w"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men sizning birinchi botingizman 🤖")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Bot ishga tushdi...")
bot.infinity_polling()
