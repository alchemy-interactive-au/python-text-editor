import tkinter as tk
# import dialogs to open & save files
from tkinter.filedialog import askopenfilename, asksaveasfilename

from tkinter.font import Font

# display a file open dialog box and store the selected file path to filepath
def open_file():
    
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # check if the user closes the dialog box or Cancels
    if not filepath:
        return
    # clear any current contents of txt_edit
    txt_edit.delete(1.0, tk.END)
    # open & read file
    with open(filepath, "r") as input_file:
        text = input_file.read()

      # iterate over this array of tuples and insert the appropriate text data or add tag information to the text widget. 

        # assigns the string text to txt_edit
        txt_edit.insert(tk.END, text)
    # set window title with the path of the open file
    window.title(f"Wordz Text Editor - {filepath}")

# display a file save dialog box - extract text in txt_edit and write to file
def save_file():
    # get save location from user and store in the filepath variable
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    # check if the user closes the dialog box or Cancels
    if not filepath:
        return

    with open(filepath, "w") as output_file: # create new file
        # text = txt_edit.get(1.0, tk.END) # extract text and assign to "text"
        # output_file.write(text) # write text to output file
        output_file.write(str(txt_edit.dump(1.0, tk.END)))

    window.title(f"Wordz Text Editor - {filepath}") # updates window title with filepath

def bold():
  # exception is raised if not text is selected
  try:
    selection = txt_edit.selection_get()
    print(selection)
  except:
    return  
  # configuring a tag with a certain style (font color)
  # Creates a bold font
  # bold_font = Font(family="Helvetica", size=14, weight="bold")
  bold_font = Font(weight="bold")  
  txt_edit.tag_configure("BOLD", font=bold_font)
  
  txt_edit.tag_add("BOLD", "sel.first", "sel.last")

  # selection.tag_configure("red", foreground="red")

  # apply the tag "red" 
  # selection.highlight_pattern("word", "red")
def highlight():
  # exception is raised if not text is selected
  try:
    selection = txt_edit.selection_get()
    print(selection)
  except:
    return  
  # configuring a tag with a certain style (font color)
  # Creates a bold font
  # bold_font = Font(family="Helvetica", size=14, weight="bold")
  # bold_font = Font(weight="bold")  
  txt_edit.tag_configure("HIGHLIGHT", background="yellow", foreground="red")
  
  txt_edit.tag_add("HIGHLIGHT", "sel.first", "sel.last")

  # selection.tag_configure("red", foreground="red")

  # apply the tag "red" 
  # selection.highlight_pattern("word", "red")

def clear():
  # exception is raised if not text is selected
  try:
    selection = txt_edit.selection_get()
    print(selection)
  except:
    return  
  txt_edit.tag_remove("BOLD",  "1.0", 'end')
  txt_edit.tag_remove("HIGHLIGHT",  "1.0", 'end')

# create new window
window = tk.Tk()
window.title("Wordz Text Editor")

# row and column configurations
window.rowconfigure(0, minsize=800, weight=1) # first column
window.columnconfigure(1, minsize=800, weight=1) # second column

# create widgets
txt_edit = tk.Text(window)
#  LH button column
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

ed_buttons = tk.Frame(fr_buttons, relief=tk.RAISED, bd=2)

# define font
myFont = Font(family='Helvetica', size=10, weight='bold')

btn_bold = tk.Button(
    master=ed_buttons,
    text= 'B',
    font='sans 16 bold',
    # font=("Helvetica", 16),
    command=bold, 
    foreground="black",
    background="white"
)
# apply font to the button label
btn_bold['font'] = myFont

btn_highlight = tk.Button(
    master=ed_buttons,
    text= 'HL',
    # font=("Helvetica", 16),
    command=highlight,
    foreground="black",
    background="yellow" 
)

btn_clear = tk.Button(
    master=ed_buttons,
    text= 'X',
    # font=("Helvetica", 16),
    command=clear,
    foreground="black",
    background="white" 
)

# geometry management
# stack buttons vertically
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

btn_bold.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
btn_highlight.grid(row=0, column=1, sticky="ew", padx=2)
btn_clear.grid(row=1, column=0, sticky="ew", padx=2)

# set up the grid layout for the rest of the window
fr_buttons.grid(row=0, column=0, sticky="ns")
ed_buttons.grid(row=3, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()


# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry.html
# https://stackoverflow.com/questions/4073468/how-do-i-get-a-selected-string-in-from-a-tkinter-text-box

# https://stackoverflow.com/questions/14786507/how-to-change-the-color-of-certain-words-in-the-tkinter-text-widget/30339009

# https://www.geeksforgeeks.org/change-the-color-of-certain-words-in-the-tkinter-text-widget/

# https://pythonexamples.org/python-tkinter-button-change-font/#5

# https://stackoverflow.com/questions/49195601/python-tkinter-saving-text-and-keeping-text-format/49196452

"""
[('mark', 'current', '1.0'), ('text', 'Hello', '1.0')]
"""
