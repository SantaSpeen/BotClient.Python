from tkinter import Menu, ttk
from tkinter.dialog import Dialog
from tkinter.simpledialog import askstring

from . import shows

from .tab_settings import settings


class BarMenu:

    def __init__(self, menu, tabs):
        self.menu = menu
        self.tabs = tabs

    @classmethod
    def select(cls, text, strings: list or dict):
        Dialog(None, title="Выбери!", text=text, strings=strings, bitmap="questhead", default=0)

    @classmethod
    def input(cls, text):
        askstring("Ввод", text)

    @classmethod
    def about(cls):
        if not shows.yesno("Версия: 0.7.1\nБилд: 161-Beta\nРазраб: Максим Хомутов", "О клиенте"):
            shows.error("ВСМЫсЛЕ НЕТ?!\nА по лбу?")

    def settings(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text='Настройки')
        settings(tab).create()

    def create(self, window):
        file = Menu(self.menu, tearoff=0)
        file.add_command(label="О клиенте", command=self.about)
        file.add_command(label="Выход", command=window.quit)
        self.menu.add_cascade(label="Файл", menu=file)

        edit_menu = Menu(self.menu, tearoff=0)
        edit_menu.add_command(label="Настройки", command=self.settings)
        self.menu.add_cascade(label="Редактировать", menu=edit_menu)
