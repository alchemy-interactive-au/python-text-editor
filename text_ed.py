import tkinter as tk

window = tk.Tk()
text_box = tk.Text()

# get text - line / character
# text_box.get("1.0")
#  get all text in text box
text_box.get("1.0", tk.END)
text_box.pack()

# insert text
text_box.insert("1.0", "Hello")

if text_box.tag_ranges(text_box.SEL):
    print('SELECTED Text is %r' % text_box.get(text_box.SEL_FIRST, text_box.SEL_LAST))
else:
    print('NO Selected Text')

    
# Tell Python to run the Tkinter event loop. This method listens for events
window.mainloop()