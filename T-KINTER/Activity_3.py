# 1) Import everything from `tkinter` to create the GUI.
from tkinter import *
# 2) Create the main window using `root = Tk()`.
windows = Tk()
# 3) Set the window title using `root.title('Number Pad')`
windows.title('Number Pad')
windows.geometry('250x300')
nums = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

for i in range(4):
    windows.rowconfigure(i, weight=1)
    windows.columnconfigure(i, weight=1)
    
    for j in range(3):
        frame = Frame(windows, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j, sticky='nsew')
        
        label = Label(frame, text=nums[i][j], bg='lightgray')
        label.pack(expand=True, fill='both', padx=5, pady=5)

windows.mainloop()
# 5) Use an outer loop to build 4 rows (i from 0 to 3):

# a) Configure the root grid columns to resize nicely using `root.columnconfigure(...)`.

# b) Configure the root grid rows to resize nicely using `root.rowconfigure(...)`.

# 6) Inside each row, use an inner loop to build 3 columns (j from 0 to 2):

# a) Create a `Frame` for each keypad cell:

# - Attach it to `root`

# - Give it a sunken border style using `relief=SUNKEN`

# - Set border thickness using `borderwidth=1`

# b) Place the frame in the grid using `frame.grid(row=i, column=j)`.

# 7) Create a `Label` inside each frame:

# a) Set label text as the corresponding value from `nums[i][j]`.

# b) Set a background color for the label.

# c) Pack the label inside the frame with padding.

# 8) Start the GUI event loop using `root.mainloop()`

# so the window remains open and responds to user actions.