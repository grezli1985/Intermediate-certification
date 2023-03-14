from datetime import datetime
from Note import *
import os
import datetime
os.system('cls')


def printAllData(data):
    if len(data) > 0:
        for object in data:
            print(object.printNote())
    else:
        print("Заметки пусты!")


def printSortedData(data):
    if len(data) > 0:
        data = sorted(data, key=lambda x: datetime.datetime.strptime(
            x.date, '%d-%m-%Y %H:%M'), reverse=True)
        for object in data:
            print(object.printNote())
    else:
        print("Заметки пусты!")


def printSpecificData(data):
    if len(data) > 0:
        index = input("Введите заметку, которую вы хотите видеть по ее id: ")
        try:
            i = int(index)
            if (i < len(data)):
                print(data[i].printNote())
            else:
                print(
                    "Неправильный ввод, убедитесь, что вы не ввели число больше, чем notes amount!")
        except ValueError:
            print("Неверный ввод, пожалуйста, введите число!")
    else:
        print("Заметки пусты!")
