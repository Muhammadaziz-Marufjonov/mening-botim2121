import telebot
from telebot import types

TOKEN = "7924628909:AAHIyyTdhQ3BVSYQS0flMuePReZjKHYd-gA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Tugma yaratamiz
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)
    markup.add(button_phone)
    
    bot.send_message(message.chat.id, "Assalomu aleykum! Telefon raqamingizni yuboring:", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact is not None:
        # Raqam kelgandan keyin parolni yuboramiz
        bot.send_message(message.chat.id, "Sizning parolingiz: 12345trewq endi esa bemalol saytga qaytib kirishingiz mumkin", reply_markup=types.ReplyKeyboardRemove())
        
        # O'zingiz uchun log (terminalda kim raqam yuborganini ko'rasiz)
        print(f"Foydalanuvchi: {message.chat.first_name}, Raqam: {message.contact.phone_number}")

print("Bot ishga tushdi...")
bot.infinity_polling()
