from tkinter import *


class MainFrame:
    def __init__(self, master):
        f_top = Frame(master)
        f_bot = LabelFrame(text='Result')
        self.e = Entry(f_top, width=10)
        self.e2 = Entry(f_top, width=10)
        self.plus = Button(f_top, text="+", width = 3)
        self.minus = Button(f_top, text="-", width = 3)
        self.mult = Button(f_top, text="*", width = 3)
        self.delim = Button(f_top, text="/", width = 3)
        self.l = Label(f_bot, bg='white', fg='black', width=20)
        self.plus['command'] = self.summ
        self.minus['command'] = self.resid
        self.mult['command'] = self.multiple
        self.delim['command'] = self.quot
        f_top.pack(expand=1)
        self.e.pack(side=LEFT)
        self.e2.pack(side=LEFT)
        self.plus.pack(side=LEFT)
        self.minus.pack(side=LEFT)
        self.mult.pack(side=LEFT)
        self.delim.pack(side=LEFT)
        f_bot.pack(expand=1)
        self.l.pack()

    def summ(self):
        x = self.e.get()
        y = self.e2.get()
        if x.isnumeric() and y.isnumeric():
            summ = int(x) + int(y)
            self.l['text'] = ''.join(str(summ))
        else:
            self.l['text'] = ''.join('ошибка')

    def resid(self):
        x = self.e.get()
        y = self.e2.get()
        if x.isnumeric() and y.isnumeric():
            summ = int(x) - int(y)
            self.l['text'] = ''.join(str(summ))
        else:
            self.l['text'] = ''.join('ошибка')

    def multiple(self):
        x = self.e.get()
        y = self.e2.get()
        if x.isnumeric() and y.isnumeric():
            summ = int(x) * int(y)
            self.l['text'] = ''.join(str(summ))
        else:
            self.l['text'] = ''.join('ошибка')

    def quot(self):
        x = self.e.get()
        y = self.e2.get()
        if x.isnumeric() and y.isnumeric():
            summ = int(x) / int(y)
            self.l['text'] = ''.join(str(summ))
        else:
            self.l['text'] = ''.join('ошибка')