from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.insert(END, "0")
entry.get()
entry.grid(row=0, column=1)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# is equal to Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

# Km value Label
km_val_label = Label(text="0")
km_val_label.grid(row=1, column=1)

# Km Label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# Button
def on_button_click():
    converted_value = round(float(entry.get()) * 1.609, 2)
    km_val_label.config(text=converted_value)

button = Button(text="Calculate", command=on_button_click)
button.grid(row=2, column=1)


window.mainloop()