import tkinter as tk
from tkinter import *


window = tk.Tk()
label = tk.Label(text="Skriv dit id")
entry = tk.Entry()
label.pack()
entry.pack()
name = entry.get()


window.mainloop()
