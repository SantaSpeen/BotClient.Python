from tkinter import *
from tkinter import ttk

from .tab0 import job
from .tab1 import stattistics

from .bar_menu import BarMenu

root = Tk()  # Основной класс
root.title("Клиент состояния бота.")  # Задаём название для окна

# Выставляем стандартное разрешение окна
root.geometry('740x480')  # linux
# window.geometry('750x445')  # Windows

# Работа с вкладками
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill='both')  # Пакуем

# Создаём фреймы для работы с вкладками
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)

# Создаём вклаку "Работа"
tab_control.add(tab0, text='Работа')  # Добовляем вкладку в ttk.Notebook
job(tab0).create()  # Отрисовываем вкладку

# Создаём вклаку "Статистика"
tab_control.add(tab1, text='Статистика')  # Добовляем вкладку в ttk.Notebook
stattistics(tab1).create()  # Отрисовываем вкладку

# Вверхнее меню
bar_menu = Menu(root)  # Материнский класс меню
root.config(menu=bar_menu)  # Добавляем в основной класс
BarMenu(bar_menu, tab_control).create(root)  # Отрисовываем


def start():
    root.mainloop()


if __name__ == '__main__':
    start()
