import tkinter as tk
from tkinter import filedialog
from tkinter import *
import wc_function as wf


def enterorder():
    order = en.get()

    btn = Button(tiw, text="choose your file", command=choose_file(order))
    btn.pack()


def choose_file(order):
    global tiw
    file_path = filedialog.askopenfilename()
    doing(order, file_path)


def doing(order, file_path):
    global tiw
    out_put = Listbox(tiw)
    if order == '-c':
        file = open(file_path, 'r')
        list1 = file.read()
        str_out = ('Char number->', len(list1.replace('\n', '')))
    elif order == '-w':
        file = open(file_path, 'r')
        str_out = ('word number->', len(re.split(r'[^a-zA-Z]+', file.read())))
    elif order == '-l':
        file = open(file_path, 'r')
        str_out = ('line number->', len(file.readlines()))
    out_put.insert(0, str_out)
    out_put.pack()

tiw = Tk()
tiw.title("wc.exe")
tiw.geometry("400x300")

en = Entry(tiw, show=None)
en.pack()
btn = Button(tiw, text="输入指令", command=enterorder).pack()

la = Label(tiw).pack()
tiw.mainloop()


