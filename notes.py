# Tutorial
# https://realpython.com/python-gui-tkinter/

import tkinter as tk

# create a new window and assign it to the variable window
window = tk.Tk()

# Create a widget. Use the tk.Label class to add text to a window
# greeting = tk.Label(text="Hello, Tkinter")

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=50,
    height=10
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry(fg="yellow", bg="blue", width=50)
name = entry.get()
entry.delete(0)



# Add widget to the window
label.pack()
# button.pack()
entry.pack()

# Tell Python to run the Tkinter event loop. This method listens for events
window.mainloop()


