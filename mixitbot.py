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
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False)
            button_download_fl_studio = types.KeyboardButton(text="FLStudio")
            button_download_manual = types.KeyboardButton(text="Мануалы")
            button_download_instr = types.KeyboardButton(text="Инструменты")
            button_download_effect = types.KeyboardButton(text="Эффекты")
            button_download_pack = types.KeyboardButton(text="Паки")
            back = types.KeyboardButton(text="Назад")

            keyboard.add(button_download_manual, button_download_instr,button_download_effect, button_download_pack, back)

            bot.send_message(message.chat.id, "Выбери продукт в меню", reply_markup=keyboard)

        elif message.text == "Назад":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button_join = types.KeyboardButton(text="Канал MIX_IT_YOURSELF")
            button_download = types.KeyboardButton(text="Скачать")

            keyboard.add(button_join, button_download)

            bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard)

        elif message.text == "FLStudio":
            bot.send_message(message.chat.id, "Ссылка на папку с FLStudio: https://disk.yandex.ru/d/W6Sc4jj1KJ9G2w")
        elif message.text == "Мануалы":
            bot.send_message(message.chat.id, "Ссылка на папку с мануалами: https://yadi.sk/d/6ct4ntzyVV_9DQ")
        elif message.text == "Инструменты":
            bot.send_message(message.chat.id, "Ссылка на папку с VST-инструментами: https://yadi.sk/d/MQ9KyV1fahXjWQ")
        elif message.text == "Эффекты":
            bot.send_message(message.chat.id, "Ссылка на папку с VST-эффектами: https://yadi.sk/d/d0WBy9JvPNpaHQ")
        elif message.text == "Паки":
            bot.send_message(message.chat.id, "Ссылка на папку с драм и миди-паками: https://yadi.sk/d/eC6dVRwv0sx_eA")


bot.polling(none_stop=True)