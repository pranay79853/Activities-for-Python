# 1) Import everything from `tkinter` to build the GUI.
from tkinter import *
# 2) Create the main window using `root = Tk()`.
windows = Tk()
windows.title('Login App')
windows.geometry('400x400')
windows.configure(bg='lightblue')
frame = Frame(windows, height=300, width=300, bg='lightgray')
lbl1 = Label(frame, text = "Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text = "Email Id", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text = "Enter Password", bg="#3895D3", fg='white', width=12)
name_entry = Entry(frame, width=20)
email_entry = Entry(frame, width=20)
pass_entry = Entry(frame, width=20, show="*")

def display():
    name = name_entry.get()
    greeting = f"Hello {name}!"
    message = "Your account has been created successfully."
    textbox.insert(END, greeting + "\n" + message + "\n")

textbox = Text(windows, height=5, width=40)
btn = Button(frame, text="Create Account", command=display, bg="#3895D3", fg='white')
frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)
windows.mainloop()
# 3) Set window properties:

# a) Set the title to "Login App".

# b) Set the window size to 400x400.

# 4) Create a `Frame` widget to organize the form elements:

# a) Attach the frame to `root`.

# b) Set height, width, and background color.

# 5) Create three labels inside the frame:

# a) Label for Full Name.

# b) Label for Email Id.

# c) Label for Password.

# (Set background color, text color, and width for each label.)

# 6) Create Entry widgets inside the frame for user input:

# a) `name_entry` for full name input.

# b) `email_entry` for email input.

# c) `pass_entry` for password input with hidden characters using `show="*"`.

# 7) Define a function `display()` that runs when the button is clicked:

# a) Get the entered name using `name_entry.get()`.

# b) Create a greeting message using the name.

# c) Create a confirmation message for account creation.

# d) Insert the greeting and message into the `textbox` using `textbox.insert(...)`.

# 8) Create a `Text` widget named `textbox` to display output messages.

# 9) Create a Button widget `btn`:

# a) Set text to "Create Account".

# b) Set `command=display` so clicking the button calls the `display()` function.

# c) Set the button background color.

# 10) Arrange all widgets using `place()`:

# a) Place the frame on the window.

# b) Place each label and its corresponding entry box.

# c) Place the button below the input fields.

# d) Place the textbox at the bottom to show messages.

# 11) Start the GUI event loop using `root.mainloop()`

# so the window stays open and responds to user actions.