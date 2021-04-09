import tkinter as tk
from tkinter import *

#def
def click():
    entered_text=textentry.get() #samler teksten fra knappen
    output.delete(0.0, END)
    try:
        password = kodeord[entered_text]
    except:
        password = "Kodeordet er forkert"
    output.insert(END, password)

#main:
window = Tk()
window.title("Depot htx hjørring: forside")
window.configure(background="white")

#Photo:
#photo = PhotoImage(file="dwight.jpeg")
#Label(window, image=photo, bg="black").grid(row=1, column=0, sticky=W)

#create label:
Label(window, text="Skriv dit kodeord:", bg="white", fg="black", font="none 12 bold").grid(row=1,column=2, sticky=N)

#Text entry:
textentry = Entry(window, width=30, bg="white")
textentry.grid(row=2, column=2, sticky=N)

#Button:
Button(window, text="FORTSÆT", width = 6, command=click).grid(row=3, column=2, sticky=N)

#ny label:
Label(window, text="\nStatus på kodeord:", bg="white", fg="black", font="none 12 bold").grid(row=4, column=2, sticky=W)

#text boks:
output = Text(window, width=30, height=1, wrap=WORD, background="white")
output.grid(row=5, column=2, columnspan=1, sticky=W)

#exit label:
Button(window, text="Forlad", width = 7, command=close_window).grid(row=8,column=2, sticky=N)
def close_window():
    window.destroy()
    exit()


#Show window:
kodeord = {'andl':'Kodeordet er godkendt','niels':'Kodeordet er godkendt','jakob':'Drengen er eftersøgt'}

#Label.pack()
window.mainloop()

#######SCAN_VARER#######
scan = Tk()
scan.title("Depot htx hjørring: scan")
scan.configure(background="white")
