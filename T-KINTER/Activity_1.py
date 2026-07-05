from tkinter import *

windows = Tk()
windows.title("My First GUI")
windows.attributes('-fullscreen', True)
windows.geometry()

def minimize(event = None):
    windows.iconify()

windows.bind("<Escape>", minimize)
windows.mainloop()