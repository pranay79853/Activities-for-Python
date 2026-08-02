from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
windows = Tk()
windows.title("Message Box")
windows.geometry("200x200")

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(windows, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
windows.mainloop()