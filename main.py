from model import detect, init_model
from telebot import TeleBot 
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.environ['TOKEN']
bot = TeleBot(TOKEN)


init_model('model/keras_model.h5','model/labels.txt')


@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, 'привет,,я помогаю сортировать мусор!!!!!!!!!!!')


@bot.message_handler(content_types=['photo'])
def image(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    file = bot.download_file(file_info.file_path)
    with open('photo.jpg', 'wb') as f:
        f.write(file)


bot.polling()
