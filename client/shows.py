from tkinter import messagebox


def error(text):
    messagebox.showerror('Ошибка!', text)


def info(text):
    messagebox.showinfo("Уведомление!", text)

def yesno(text, title="Выбери"):
    messagebox.askyesno(title, text)