from tkinter import *
from tkinter import ttk

from .bar_menu import selector

from .tab0 import job
from .tab1 import stattistics
# from .tab2 import settings

host: str
token: str

window = Tk()
window.title("Клиент состояния бота.")
window.geometry('750x445')

# Работа с вкладками
tab_control = ttk.Notebook(window)
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)

tab_control.add(tab0, text='Работа')
job(tab0).create()

tab_control.add(tab1, text='Статистика')
stattistics(tab1).create()

# Вверхнее меню
bar_menu = Menu(window)
window.config(menu=bar_menu)
selector(bar_menu, tab_control).create(window)

tab_control.pack(expand=1, fill='both')
window.mainloop()
