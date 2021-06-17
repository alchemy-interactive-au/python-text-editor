import tkinter as tk

convert_to = "cel"

# conversion function
def fahrenheit_to_celsius(*args):
  # *args required to prevent errors when keystroke binds send event arguments
  global convert_to
  # get imput
  temperature = ent_temperature.get()
  print(temperature)

  # error checking - check if number!!!
  try:
    val = int(temperature)
  except ValueError:
    lbl_result["text"] = "Invalid input"
    return

  if convert_to == "cel":
    # print("converting to cel")
    celsius = (float(temperature) - 32) * (5/9) # conversion formula
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}" #assign to var

  else:
    # print("converting to far")
    fahrenheight = (float(temperature) * 1.8) + 32 # conversion formula
    lbl_result["text"] = f"{round(fahrenheight, 2)} \N{DEGREE FAHRENHEIT}" #assign to var    

     
# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
# window.resizable(width=False, height=False)

# configure resize options - weight controls relative changes
window.columnconfigure(0, weight=1, minsize=350) # column width
window.rowconfigure([0, 1, 2], weight=1, minsize=50) # row height

# Create the Fahrenheit entry frame with an Entry widget and label in it
frm_entry = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
# entry box config - inside frame container
ent_temperature = tk.Entry(master=frm_entry, width=10, justify='center')
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}", bg="lightgrey", fg="green")
# placeholder text
ent_temperature.insert(0, '451')

# toggle conversion direction
def toggle_convert():
  global convert_to # refer to global var

  # update labels based on direction
  if convert_to == "cel":
    convert_to = "far"
    lbl_temp.configure(text="\N{DEGREE CELSIUS}", fg="blue")
    lbl_result.configure(text="0 \N{DEGREE FAHRENHEIT}", fg="blue")
    lbl_temp.update()
    lbl_result.update()

  else: 
    convert_to = "cel"
    lbl_temp.configure(text="\N{DEGREE FAHRENHEIT}", fg="green")
    lbl_result.configure(text="0 \N{DEGREE CELSIUS}", fg="green")
    lbl_temp.update()
    lbl_result.update()


# clear placeholder text with focus
def clear_entry(event):
  # print("click")
  ent_temperature.delete(0, tk.END)

# keyboard bindings
ent_temperature.bind("<Button-1>", clear_entry) 
window.bind('<Return>', fahrenheit_to_celsius) # allow enter button to run  
# https://stackoverflow.com/questions/42509045/tkinter-typeerror-missing-1-required-positional-argument

# toggle conversion direction button
btn_toggle = tk.Button(
    master=frm_entry,
    text= '\u21D4',
    font=("Helvetica", 16),
    command=toggle_convert, 
    foreground="white",
    background="darkgrey"
)

# Layout the temperature Entry and Label in frm_entry using the .grid() geometry manager
#  This row has 2 columns - east / west
ent_temperature.grid(row=0, column=0, sticky="w")
lbl_temp.grid(row=0, column=1, padx=5, sticky="e")
btn_toggle.grid(row=0, column=2, sticky="e")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text= '\N{RIGHTWARDS ARROW}',
    command=fahrenheit_to_celsius, 
    foreground="yellow",
    background="green"
)

# output var & options
lbl_result = tk.Label(master=window, text="? \N{DEGREE CELSIUS}", foreground="green", bg="white", highlightbackground="grey", highlightthickness=1, padx=5)

# Set-up the layout using the .grid() geometry manager
# sticky="ns" positions each label at the center of its grid cell
frm_entry.grid(row=0, column=0)
btn_convert.grid(row=1, column=0, pady=10, sticky="ns")
lbl_result.grid(row=2, column=0, pady=10, sticky="ns")

# Run the application
window.mainloop()