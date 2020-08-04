from tkinter import Button, Text, TOP, END, Frame

from .server_api import bot_stat


class stattistics:

    def __init__(self, tab):
        self.tab = tab
        self.t0 = None

    def connect(self):
        info = bot_stat()
        self.t0.delete(1.0, END)
        self.t0.insert(1.0, f'Аптайм: {info[0]}\n'
                            f'Среднее время Event: {info[1]}\n'
                            f'Сообщений принято: {info[2]}')

    def create(self):
        top = Frame(self.tab)
        top.pack()

        self.t0 = Text(top)
        self.t0.pack()
        self.t0.insert(1.0, 'Аптайм: Обновите данные\n'
                            'Среднее время Event: Обновите данные\n'
                            'Сообщений принято: Обновите данные')
        bottom = Frame(self.tab)
        bottom.pack()
        Button(bottom, text="Обновить", command=self.connect).pack(side=TOP)

