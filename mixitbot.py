import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, {0.username}! Здесь ты можешь найти полезную инфу по созданию музыки и сведению".format(message.from_user))

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_join = types.KeyboardButton(text="Канал MIX_IT_YOURSELF")
    button_download = types.KeyboardButton(text="Скачать")

    keyboard.add(button_join, button_download)

    hello = "Жми нужную кнопку в меню!"
    bot.send_message(message.chat.id, text=hello, reply_markup=keyboard)

#обработчик события нажатия на кнопки

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Канал MIX_IT_YOURSELF":
            bot.send_message(message.chat.id, "Присоединяйся! https://t.me/mix_music_tips")
        elif message.text == "Скачать":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_download_master = types.KeyboardButton(text="The Mastering Blueprint")
            button_download_mix = types.KeyboardButton(text="The Mixing Blueprint")
            button_download_compression = types.KeyboardButton(text="Ultimate Guide To Compression")
            back = types.KeyboardButton(text="Назад")

            keyboard.add(button_download_master, button_download_mix, button_download_compression, back)

            bot.send_message(message.chat.id, "Выбери продукт в меню", reply_markup=keyboard)

        elif message.text == "Назад":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button_join = types.KeyboardButton(text="Канал MIX_IT_YOURSELF")
            button_download = types.KeyboardButton(text="Скачать")

            keyboard.add(button_join, button_download)

            bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard)

        elif message.text == "The Mastering Blueprint":
            bot.send_message(message.chat.id, "Ссылка на скачивание: https://yadi.sk/i/31Eq1pAFTCGnPg")
        elif message.text == "The Mixing Blueprint":
            bot.send_message(message.chat.id, "Ссылка на скачивание: https://yadi.sk/i/pHu0bBC_rHk6iA")
        elif message.text == "Ultimate Guide To Compression":
            bot.send_message(message.chat.id, "Ссылка на скачивание: https://yadi.sk/i/KIk3NO3rtRfROQ")

bot.polling(none_stop=True)