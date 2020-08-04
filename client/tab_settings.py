import json
import traceback
from tkinter import Button, Text, Frame, LEFT, END
from tkinter.dialog import Dialog

from . import shows
from .config import open_config, save_config
from .server_api import bot_getAdmins


class settings:
    def __init__(self, tab):
        self.tab = tab
        self.t0 = None

    def send_code(self):
        Dialog(None, title="Выбери!", text="Кому выслать код?", strings=open_config()["admins"], bitmap="questhead", default=0)

    def set(self):
        try:
            global host, token
            data = self.t0.get(1.0, END)
            save_config(json.loads(data), bot_getAdmins)
            shows.info("Установки успешно приняты!")
            self.read()
            self.tab.pack_forget()
            self.tab.destroy()
        except Exception as e:
            print(traceback.format_exc())
            shows.error(f"Проверь, чо ты там ввёл\n{e}")

    def read(self):
        self.t0.delete(1.0, END)
        self.t0.insert(1.0, open_config(True))

    def create(self):
        top = Frame(self.tab)
        top.pack()

        self.t0 = Text(top)
        self.t0.pack()
        self.read()

        bottom = Frame(self.tab)
        bottom.pack()

        b0 = Button(bottom, text="Выслать код", command=self.send_code)
        b1 = Button(bottom, text="Применить", command=self.set)

        b0.pack(side=LEFT)
        b1.pack(side=LEFT)


