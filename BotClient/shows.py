from tkinter import messagebox


def error(text):
    messagebox.showerror('Ошибка!', text)


def info(text):
    messagebox.showinfo("Уведомление", text)