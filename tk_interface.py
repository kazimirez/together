from tkinter import *
from tkinter import ttk

def show_message():
    x = StringVar()
    x.set(litera.get())
    print (x.get())

if __name__ == '__main__':
    root = Tk()
    root.title("Создание БЧ детали")
    root.geometry("600x250+1700+800")

    #label = Label(text="Вверите допуск")
    #label.pack()
    litera = ttk.Entry(width=5)
    litera.grid(column=0, row=1, padx=6, pady=6)

    dim_main = ttk.Entry()
    dim_main.grid(column=1, row=1, padx=6, pady=6)

    dim_it = ttk.Entry()
    dim_it.grid(column=2,row=1, padx=6, pady=6)

    dim_upper_deviation = ttk.Entry()
    dim_upper_deviation.grid(column=3,row=0, padx=6, pady=6)

    dim_lower_deviation = ttk.Entry()
    dim_lower_deviation.grid(column=3,row=2, padx=6, pady=6)


    btn = ttk.Button(text="Click", command=show_message())
    btn.grid(column=2, row=5, padx=6, pady=6)

    x = show_message()
    print("конец", x.get())
    root.mainloop()



