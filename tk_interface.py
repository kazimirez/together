from tkinter import *
from tkinter import ttk

def show_message():
    label["text"] = entry.get()

root = Tk()
root.title("Создание БЧ детали")
root.geometry("600x250")

label = Label(text="Вверите допуск")
label.pack()

dim_main = ttk.Entry()
dim_main.pack(anchor=NW, padx=6, pady=6)

dim_it = ttk.Entry()
dim_main.pack(anchor=NW, padx=6, pady=6)

dim_upper_deviation = ttk.Entry()
dim_main.pack(anchor=NW, padx=6, pady=6)

dim_lower_deviation = ttk.Entry()
dim_main.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)


root.mainloop()