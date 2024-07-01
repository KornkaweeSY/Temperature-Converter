from tkinter import *
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงอุณหภูมิ")
root.iconbitmap("icons/tempicon.ico")
root.resizable(0, 0)

# Setting
font = ("Arial", 15, "bold")
color = "orange"

# Input widget
input_label = Label(root, text="อุณหภูมิ (Celsius)", font=font)
input_txt = Entry(root, width=20, font=font)
input_label.grid(row=0, column=0, sticky=W)
input_txt.grid(row=0, column=1)

# Choice widget
unit_label = Label(root, text="แปลงเป็นหน่วย", font=font)
unit_label.grid(row=1, column=0, sticky=W)

units = ["Celsius", "Fahrenheit", "Kelvin"]
unit_combobox = ttk.Combobox(root, values=units, font=font, state="readonly")
unit_combobox.grid(row=1, column=1)
unit_combobox.current(0)  # Set default unit to Celsius

# Output widget
output_label = Label(root, text="ผลลัพธ์", font=font)
output_label.grid(row=2, column=0, sticky=W)

output_txt = Entry(root, width=20, font=font)
output_txt.grid(row=2, column=1)

# Button widget
def convert_temperature():
    try:
        temperature = float(input_txt.get())
        unit = unit_combobox.get()

        if unit == "Celsius":
            converted_temp = temperature
        elif unit == "Fahrenheit":
            converted_temp = (temperature * 9/5) + 32
        elif unit == "Kelvin":
            converted_temp = temperature + 273.15

        output_txt.delete(0, END)
        output_txt.insert(0, f"{converted_temp:.2f}")
    except ValueError:
        output_txt.delete(0, END)
        output_txt.insert(0, "กรุณากรอกตัวเลขเท่านั้น")

convert_button = Button(root, text="แปลง", font=font, bg=color, command=convert_temperature)
convert_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
