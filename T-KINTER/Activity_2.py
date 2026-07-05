# 1) Import required libraries:
import tkinter as tk
import datetime as date
windows = tk.Tk()
windows.title("My First GUI")
windows.attributes('-fullscreen', True)
windows.geometry()

lbl = tk.Label(windows, text="Hey There!", fg="white", bg="blue", height=2, width=20)
name_lbl = tk.Label(windows, text="Please enter your full name:")
name_entry = tk.Entry(windows)

def display():
    global message
    name = name_entry.get()
    greeting = f"Hello, {name}!"
    today = date.datetime.now().strftime("%Y-%m-%d")
    message = f"{greeting}\nWelcome to the GUI application!\nToday's date is: {today}"
    text_box.insert(tk.END, message)

text_box = tk.Text(windows, height=10, width=50)
btn = tk.Button(windows, text="Begin", command=display, height=2, bg="green", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

def minimize(event = None):
    windows.iconify()

windows.bind("<Escape>", minimize)
windows.mainloop()