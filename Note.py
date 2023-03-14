import os
os.system('cls')


class Note:
    def __init__(self, title, body, date, idarg):
        self.title = title
        self.body = body
        self.date = date
        self.id = idarg

    def printNote(self):
        return "ID: {}\nTitle: {}\n {}".format(self.id, self.title, self.body)
