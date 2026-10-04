from model import detect, init_model
from telebot import TeleBot
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.environ["TOKEN"]
bot = TeleBot(TOKEN)


init_model("model/keras_model.h5", "model/labels.txt")


@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id, "привет,,я помогаю сортировать мусор!!!!!!!!!!!")


@bot.message_handler(content_types=["photo"])
def image(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    file = bot.download_file(file_info.file_path)
    with open("photo.jpg", "wb") as f:
        f.write(file)
    label, score = detect("photo.jpg")
    answer = "неизвестный тип мусора"
    if label == "bio":
        answer = """Это биологические отходы. 

        Пищевые отходы (яблоки, кожура, остатки еды) можно выбрасывать в обычный мусор или, если есть, в отдельный контейнер для органики, а лучше — компостировать."""

    elif label == "paper":
        answer = """Это бумага или картон. 

        Их можно сдать в макулатуру или выбросить в обычный мусор, а если есть отдельный контейнер для бумаги — то туда."""
    elif label == "glass":
        answer = """Это стекло.
        
        Его можно сдать в пункт приёма стеклотары или выбросить в контейнер для стекла, а при его отсутствии — в обычный мусор."""

    elif label == "plastic":
        answer = """Это пластик. 
        
        Его нужно выбросить в отдельный контейнер для пластика или сдать в пункт приёма, а при их отсутствии — в обычный мусор.

"""

    bot.send_message(message.chat.id, answer)


bot.polling()
