from tkinter import *

windows = Tk()
windows.geometry("400x300")
windows.title("main")

def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    # Adding a label widget to Top Window
    l2 = Label(top, text="This is a Top Window")
    l2.pack()

    top.mainloop()

l = Label(windows, text="This is a Main Window")
btn = Button(windows, text="Click Me", command=topwin)
l.pack()
btn.pack()

windows.mainloop()