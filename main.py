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
    