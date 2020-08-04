from tkinter import Button, TOP, END, Text, Frame

from .json_access import open_config
from .server_api import bot_isActive


class job:

    def __init__(self, tab):
        self.tab = tab
        self.t0 = None

    def connect(self):
        host = open_config()["host"]
        self.t0.delete(1.0, END)
        to_t0t0 = "Не работает.."
        if bot_isActive():
            to_t0t0 = "В работе!\nHost: " + host
        self.t0.insert(1.0, "Состояние: " + to_t0t0)

    def create(self):
        top = Frame(self.tab)
        top.pack()

        self.t0 = Text(top)
        self.t0.pack()
        self.t0.insert(1.0, 'Состояние: Не известно.')

        bottom = Frame(self.tab)
        bottom.pack()
        Button(bottom, text="Обновить", command=self.connect).pack(side=TOP)
