from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = "class-shelve"
fieldnames = ("name", "age", "job", "pay")

def makeWidgets():
    global entries
    window = Tk()
    window.title("People Shelve")
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(("key",) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text="Fetch
