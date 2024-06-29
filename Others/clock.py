from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")


def time():
    clock = strftime('%H:%M:%S')
    label.config(text=clock)
    label.after(1000, time)


label = Label(root, font=("ds_digital", 80),background="black", foreground="white")
label.pack(anchor="center")

time()

mainloop()
