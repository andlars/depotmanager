import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import messagebox

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        def click():
            entered_text=textentry.get() #samler teksten fra knappen
            output.delete(0.0, END)
            try:
                password = kodeord[entered_text]
            except:
                password = "Kodeordet er forkert"
                tk.messagebox.showerror("Kodeordet er forkert", "Det indtastede kodeord er forkert")
            output.insert(END, password)

        self.frames = {}
        for F in (StartPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start skærm", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)

        label1 = tk.Label(self, text="Brugernavn:")
        label1.pack(side="left")

        label2 = tk.Label(self)
        label2.pack(side="left")

        textentry = tk.Entry(self, width=30, bg="white")

        button2 = tk.Button(self, text="Log ind:",
                            command=lambda: controller.show_frame("PageTwo"))



        output = tk.Text(self, width=30, height=1, background="white")

        button2.pack(side="bottom", pady=50)
        textentry.pack(side="bottom", pady = 20)
        output.pack(side = "bottom", pady = 1)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=200, padx=400)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

#class PageTree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))


        button2 = tk.Button(self, text="Log ind:",
                            command=lambda: controller.show_frame("PageTwo"))

        button.pack()
