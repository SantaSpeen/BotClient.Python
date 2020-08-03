from tkinter import *
from tkinter import ttk, messagebox

from .tab0 import job
from .tab1 import stattistics
from .tab2 import settings

import json

host: str
token: str


def bot_isActive() -> bool:
    r = {"response": {"status": True}}
    return r["response"]["status"]

window = Tk()
window.title("Клиент состояния бота.")
window.geometry('400x250')

tab_control = ttk.Notebook(window)
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab0, text='Работа')
job(tab0).create()

tab_control.add(tab1, text='Статистика')
stattistics(tab1).create()

tab_control.add(tab2, text='Настройки')
settings(tab2).create()

tab_control.add(tab3, text='О клиете')
Label(tab3, text="Версия: 0.1.3\nБилд: 43-альфа\nРазраб: Максим Хомутов").pack(side='top')

tab_control.pack(expand=1, fill='both')
window.mainloop()
