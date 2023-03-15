from ImportExport import *
from PrintData import *
from Note import *
import os
import datetime
os.system('cls')


def inputData(notes):
    idarg = len(notes)
    title = input("Введите название: ")
    body = input("Введите заметку: ")
    now = datetime.datetime.now()
    return [title, body, now.strftime("%d-%m-%Y %H:%M"), idarg]


def addNote(notes):
    noteinfo = inputData(notes)
    return Note(noteinfo[0], noteinfo[1], noteinfo[2], noteinfo[3])


def seeNotesAmount(notes):
    print("Примечания количество: ", len(notes))


def editNote(notes):
    if (len(notes) > 0):
        index = input("Введите заметку, которую вы хотите отредактировать, по ее id: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes[i] = addNote(notes)
                print("Примечание изменено!")
            else:
                print("Неправильный ввод, убедитесь, что вы не ввели число больше, чем количество!")
        except ValueError:
            print("Неверный ввод, пожалуйста, введите число!")
    else:
        print("Заметки пусты!")


def deleteNote(notes):
    if (len(notes) > 0):
        index = input("Введите заметку, которую вы хотите удалить, по ее id: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes.pop(i)
                print("Примечание удалено!")
            else:
                print("Неправильный ввод, убедитесь, что вы не ввели число больше, чем количество!")
        except ValueError:
            print("Неверный ввод, пожалуйста, введите число!")
    else:
        print("Заметки пусты!")


def main():
    notes = []
    done = False
    while (done == False):
        print("Добро пожаловать в Блокнот--\n\
        выберите варианты:\n\
        1 - Импортировать заметки из файла;\n\
        2 - Экспорт заметок в файл;\n\
        3 - Создать новую заметку;\n\
        4 - Просмотреть все заметки;\n\
        5 - Просмотреть все заметки, причем самые последние отображаются первыми;\n\
        6 - Просмотр конкретной заметки;\n\
        7 - Проверьте, сколько у вас заметок;\n\
        8 - Изменить заметку;\n\
        9 - Удалить заметку;\n\
        0 - Выход.")
        command = input("Введите команду: ")
        match command:
            case "1":
                notes = importFromFile()
            case "2":
                writeToFile(notes)
            case "3":
                notes.append(addNote(notes))
                print("Примечание сохранено!")
            case "4":
                printAllData(notes)
            case "5":
                printSortedData(notes)
            case "6":
                printSpecificData(notes)
            case "7":
                seeNotesAmount(notes)
            case "8":
                editNote(notes)
            case "9":
                deleteNote(notes)
            case "0":
                print("До свидания!")
                done = True
            case _:
                print("Неверный ввод")
