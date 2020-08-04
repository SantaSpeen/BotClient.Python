from tkinter import Menu, ttk
from tkinter.dialog import Dialog
from tkinter.simpledialog import askstring

from . import shows
from .json_access import open_global_vars, save_global_vars

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
        if not shows.yesno("Версия: 0.7.3\nБилд: 167\nСтатус: Beta\nРазраб: Максим Хомутов", "О клиенте"):
            shows.error("ВСМЫсЛЕ НЕТ?!\nА по лбу?")

    def settings(self):
        if not open_global_vars()["setting_open"]:
            save_global_vars(setting_open=True)
            tab = ttk.Frame(self.tabs)  # Создаём фрейм для вкладки "Настройки"
            self.tabs.add(tab, text='Настройки')
            settings(tab).create()  # Создаём вкладкуы
        else:
            shows.info("Настройки уже открыты.")

    # Функция отрисовки бар меню
    def create(self, window):
        # Создаём каскад для меню - "Файл"
        file = Menu(self.menu, tearoff=0)
        file.add_command(label="О клиенте", command=self.about)  # Добавляем пункт "О клиенте"
        file.add_command(label="Выход", command=window.quit)  # Добавляем пункт "выход"
        self.menu.add_cascade(label="Файл", menu=file)  # Добавляем наш каскад в основное меню

        # Создаём каскад для меню - "Редактировать"
        edit = Menu(self.menu, tearoff=0)
        edit.add_command(label="Настройки", command=self.settings)  # Добавляем пункт "Настройки"
        self.menu.add_cascade(label="Редактировать", menu=edit)  # Добавляем наш каскад в основное меню
