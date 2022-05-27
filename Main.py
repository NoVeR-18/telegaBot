import openpyxl
import config
import telebot
bot = telebot.TeleBot(config.TOKEN)


class Cartoon:
    def __init__(self):
        self.name = None
        self.type = None
        self.duration = None
        self.year = None
        self.country = None
        self.genre = None


if __name__ == "__main__":
    #загрузка базы данных
    cartoon = Cartoon()
    cartoons = openpyxl.open("data.xlsx", read_only=True)
    sheet = cartoons.active
    #ввод мультфильма(ничего не введено - пропуск)
    specific = {'name': input("Enter Cartoon name"),
                'type': input("Enter Cartoon type"),
                'duration': input("Enter max duration"),
                'year': input("Enter min year"),
                'country': input("Enter Country of Origin"),
                'genre': input("Enter genre of cartoon")
                }
    while len(specific['duration']) != 0 or int(specific['duration']) < 3:
        print("mistake duration")
        specific['duration'] = input("Enter max duration")

    while int(specific['year']) < 1953 or len(specific['year']) != 0:
        print("mistake year")
        specific['year'] = input("Enter max duration")

    #подбор мультфильма согласно введенным данным
    for row in range(2, 8):
        cartoon.name = sheet[row][0].value
        cartoon.type = sheet[row][1].value
        cartoon.duration = int(sheet[row][2].value)
        cartoon.year = int(sheet[row][3].value)
        cartoon.country = sheet[row][4].value
        cartoon.genre = sheet[row][5].value
        #если мультфильм подходит по параметрам, то выводим его
        if (cartoon.name == specific['name'] or len(specific['name']) == 0) and \
                (cartoon.type == specific['type'] or len(specific['type']) == 0) and \
                (cartoon.duration <= int(specific['duration']) or len(specific['duration']) == 0) and \
                (cartoon.year >= int(specific['year']) or len(specific['year']) == 0) and \
                (cartoon.country == specific['country'] or len(specific['country']) == 0) and \
                (cartoon.genre == specific['genre'] or len(specific['genre']) == 0):
            print(cartoon.name, cartoon.type, cartoon.duration, cartoon.year, cartoon.country, cartoon.genre)
