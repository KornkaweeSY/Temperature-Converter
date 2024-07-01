from tkinter import *
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงอุณหภูมิ")
root.iconbitmap("icons/tempicon.ico")
root.resizable(0, 0)

def convert():
    output_txt.delete(0, END)

    #ตัวเลขที่ผู้ใช้ป้อน
    celsius_value = float(input_txt.get())

    #หน่วยที่ผู้ใช้เลือก
    unit_value = temp_combo.get()
    
    #คำนวน
    if unit_value == "Kelvin":
        kelvin = celsius_value + 273
        output_txt.insert(0, kelvin)
    else:
        fahrenheit = celsius_value * 1.8 + 32
        output_txt.insert(0, fahrenheit)

def reset():
    output_txt.delete(0, END)
    input_txt.delete(0, END)
    temp_combo.set("Kelvin")

#setting
font = ("Arail", 15, "bold")
color = "orange"

#input widget
input_label = Label(root, text="อุณหภูมิ (Celsius)", font=font)
input_txt = Entry(root, width=20, font=font)
input_label.grid(row=0, column=0, sticky=W)
input_txt.grid(row=0, column=1)

#choice widget
unit_label = Label(root, text="แปลงเป็นหน่วย", font=font)
unit_list = ["Fahrenheit", "Kelvin"]
temp_combo = ttk.Combobox(root, value= unit_list, font=font, width=18)
temp_combo.set("Kelvin")
unit_label.grid(row=1, column=0, sticky=W)
temp_combo.grid(row=1, column=1)

#output widget
output_label = Label(root, text="Summary", font=font)
output_txt = Entry(root, width=20, font=font)
output_label.grid(row=2, column=0, sticky=W)
output_txt.grid(row=2, column=1)

#button widget
convertBtn = Button(root, text="Change", font=font, width=10, bg=color, command=convert)
resetBtn = Button(root, text="Reset", font=font, width=7, bg=color, command=reset)
convertBtn.grid(row=3, column=1, sticky=W, padx=5, pady=5)
resetBtn.grid(row=3, column=1, sticky=E, padx=5, pady=5)


root.mainloop()