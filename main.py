from leafan import *

# Ошибка 32: компас не запущен
# Ошибка 33: Документ не является деталью

if __name__ == '__main__':
    print(kompas_check())
    if not kompas_check():
        exit(32)


    api5, api7, kompas_document, kompas_object, application, kompas_document_3d = connectAPI()
    main_lfn()

    part7 = kompas_document_3d.TopPart
    propertyMng = api7.IPropertyMng(application)
    propertyKeeper = api7.IPropertyKeeper(part7)


    def set_property(property_name, value):
        for i in range(propertyMng.PropertyCount(kompas_document)):
            property = propertyMng.GetProperty(kompas_document, i)
            if property.Name == property_name:
                propertyKeeper.SetPropertyValue(property, value, True)
                return property
            i += 1


    def get_property_value(propertyName):
        i = 0
        for i in range(propertyMng.PropertyCount(kompas_document)):
            property = propertyMng.GetProperty(kompas_document, i)
            if property.Name == propertyName:
                propertyVal = propertyKeeper.GetPropertyValue(property, "", True, True)
                return propertyVal[1]


    def create_property():
        pass

    # Проверка на то, что документ является чертежом
    if kompas_document.DocumentType != 4:
        application.MessageBoxEx("Данный макрос работает только с деталью", "Документ не является деталью", 0)
        exit(33)
    # Возвращает имя детали с чертежом
    real_name = to_drawing(get_property_value("Наименование"))
    set_property("Наименование", real_name)


    #----------------------------------------------------------------------------------------------------------------Tk

    def set_dimension():
        dim = Dimension(dim_main.get())
        dim.set_lower_deviation(dim_lower_deviation.get())
        dim.set_upper_deviation(dim_upper_deviation.get())
        print(dim.print_tolerance(True, True))
        set_property("Форматы листов документа", "БЧ")
        bche_name = get_property_value("Наименование") + "@/" + get_property_value("Материал") + "@/" + litera.get() + dim.print_tolerance(True, True)
        set_property("Наименование", bche_name)
        set_property("Примечание", smartRound(get_property_value("Масса")))
        exit(23)

    #root = ThemedTk(theme="scid themes")
    root = Tk()
    s = ttk.Style()
    s.theme_use('clam')
    root.title("Создание БЧ детали")
    root.geometry("600x250+1700+800")
    print(s.theme_use())
    label = Label(text="Размер").grid(column=1, row=0, padx=6, pady=6)
    label2 = Label(text="Класс точности").grid(column=2, row=0, padx=6, pady=6)
    label3 = Label(text="Допуск").grid(column=3, row=1, padx=6, pady=6)

    litera = ttk.Entry(width=4, justify=CENTER)
    litera.grid(column=0, row=1, padx=6, pady=6)
    litera.insert(0, "L = ")

    dim_main = ttk.Entry(width=7, justify=CENTER)
    dim_main.grid(column=1, row=1, padx=6, pady=6)

    dim_it = ttk.Entry(width=7, justify=CENTER)
    dim_it.grid(column=2,row=1, padx=6, pady=6)

    dim_upper_deviation = ttk.Entry(width=7, justify=CENTER)
    dim_upper_deviation.grid(column=3,row=0, padx=6, pady=6)

    dim_lower_deviation = ttk.Entry(width=7, justify=CENTER)
    dim_lower_deviation.grid(column=3,row=2, padx=6, pady=6)


    btn = ttk.Button(text="Click", command=set_dimension)
    btn.grid(column=2, row=5, padx=6, pady=6)


    root.mainloop()

    #------------------------------------------------------------------------------------------------------------------
