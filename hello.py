#!/usr/bin/python3.5

from tkinter import *

root = Tk()
root.geometry("320x40")

text = Text(root)
text.pack(fill=BOTH)

text.insert(END, "Hello world!")
text.config(state='disabled')

root.mainloop()

