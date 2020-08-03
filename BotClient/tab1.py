from tkinter import Button, Text, TOP, END


class stattistics:

    def __init__(self, tab):
        self.tab = tab
        self.t0 = None

    def connect(self):
        r = {"response": {"uptime": "16 м 20 с", "event_time": "0.123132", "message_counter": "13"}}
        r = r["response"]
        info = [r["uptime"], r["event_time"], r["message_counter"]]
        self.t0.delete(1.0, END)
        self.t0.insert(1.0, f'Аптайм: {info[0]}\n'
                         f'Среднее время Event: {info[1]}\n'
                         f'Сообщений принято: {info[2]}')

    def create(self):
        Button(self.tab, text="Обновить", command=self.connect).pack(side=TOP)
        self.t0 = Text(self.tab)
        self.t0.pack()
        self.t0.insert(1.0, 'Аптайм: Обновите данные\n'
                         'Среднее время Event: Обновите данные\n'
                         'Сообщений принято: Обновите данные')