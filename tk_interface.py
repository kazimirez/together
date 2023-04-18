from tkinter import *
from tkinter import ttk
from leafan import *

def set_dimension():
    dim = Dimension(dim_main.get())
    print(dim.print_tolerance(True, True))

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


    btn = ttk.Button(text="Click", command=set_dimension)
    btn.grid(column=2, row=5, padx=6, pady=6)


    print("конец")
    root.mainloop()



