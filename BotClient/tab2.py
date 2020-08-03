import json
import traceback
from tkinter import Button, Text, TOP, END

from . import shows
from .config import open_config, save_config


class settings:
    def __init__(self, tab):
        self.tab = tab
        self.t0 = None

    def set(self):
        try:
            global host, token
            data = self.t0.get(1.0, END)
            save_config(json.loads(data))
            shows.info("Установки успешно приняты!")
        except Exception as e:
            print(traceback.format_exc())
            shows.error(f"Проверь, чо ты там ввёл\n{e}")

    def read(self):
        self.t0.insert(1.0, open_config(True))

    def create(self):
        Button(self.tab, text="Применить", command=self.set).pack(side=TOP)
        self.t0 = Text(self.tab)
        self.t0.pack()
        self.read()
