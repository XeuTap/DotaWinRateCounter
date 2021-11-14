from tkinter import *


class Resolve:
    def __init__(self, master):
        f_top = LabelFrame(text='Matches------Wins')
        f_bot = LabelFrame(text='Result')
        self.e = Entry(f_top, width=10)
        self.e2 = Entry(f_top, width=10)
        self.plus = Button(f_top, text="calculate", width = 12)
        self.label = Label(f_bot, bg='white', fg='black', width=20)
        self.plus['command'] = self.calculate
        f_top.pack(expand=1)
        self.e.pack(side=LEFT)
        self.e2.pack(side=LEFT)
        self.plus.pack()
        f_bot.pack(expand=1)
        self.label.pack()

    def calculate(self):
        total = self.e.get()
        matches = self.e2.get()
        if total.isnumeric() and matches.isnumeric():
            summ = int(matches) / int(total) * 100
            summ = round(summ, 2)
            self.label['text'] = ''.join(str(summ) + '%')
        else:
            self.label['text'] = ''.join('ошибка')