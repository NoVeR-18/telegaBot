import openpyxl

import config
import telebot

class Cartoon:
    def __init__(self):
        self.name = None
        self.type = None
        self.duration = None
        self.year = None
        self.country = None
        self.genre = None


specific = {'name': "", 'type': "", 'duration': "", 'year': "", 'country': "", 'genre': ""}

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """enter characteristic""")

@bot.message_handler(content_types=['text'])
def text(message):
    # bot.send_message(message.chat.id, message.text)
    if message.text == "name":
        msg = bot.send_message(message.chat.id, 'enter Name')
        bot.register_next_step_handler(msg, name)
    elif message.text == "type":
        msg = bot.send_message(message.chat.id, 'enter type')
        bot.register_next_step_handler(msg, type)
    elif message.text == "duration":
        msg = bot.send_message(message.chat.id, 'enter duration')
        bot.register_next_step_handler(msg, duration)
    elif message.text == "year":
        msg = bot.send_message(message.chat.id, 'enter year')
        bot.register_next_step_handler(msg, year)
    elif message.text == "country":
        msg = bot.send_message(message.chat.id, 'enter country')
        bot.register_next_step_handler(msg, country)
    elif message.text == "genre":
        msg = bot.send_message(message.chat.id, 'enter genre')
        bot.register_next_step_handler(msg, genre)
    elif message.text == "final":
        find(message)

def name(message):
    specific['name'] = message.text

def type(message):
    specific['type'] = message.text
def duration(message):
    specific['duration'] = message.text
def year(message):
    specific['year'] = message.text
def country(message):
    specific['country'] = message.text
def genre(message):
    specific['genre'] = message.text
def final(message):
    find(message)


def find(message):
    # загрузка базы данных
    cartoon = Cartoon()
    cartoons = openpyxl.open("data.xlsx", read_only=True)
    sheet = cartoons.active

    # подбор мультфильма согласно введенным данным
    for row in range(2, 8):
        cartoon.name = sheet[row][0].value
        cartoon.type = sheet[row][1].value
        cartoon.duration = int(sheet[row][2].value)
        cartoon.year = int(sheet[row][3].value)
        cartoon.country = sheet[row][4].value
        cartoon.genre = sheet[row][5].value
        # если мультфильм подходит по параметрам, то выводим его
        if (cartoon.name == specific['name'] or len(specific['name']) == 0) and \
                (cartoon.type == specific['type'] or len(specific['type']) == 0) and \
                (cartoon.country == specific['country'] or len(specific['country']) == 0) and \
                (cartoon.genre == specific['genre'] or len(specific['genre']) == 0):
            bot.send_message(message.chat.id, cartoon.name)
            bot.send_message(message.chat.id, cartoon.type)
            bot.send_message(message.chat.id, cartoon.duration)
            bot.send_message(message.chat.id, cartoon.year)
            bot.send_message(message.chat.id, cartoon.country)
            bot.send_message(message.chat.id, cartoon.genre)

bot.polling(none_stop=True);
