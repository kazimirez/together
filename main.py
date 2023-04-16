from leafan import *
from tkinter import *
#from kazimir import replacer

#Ошибка 32: компас не запущен
#Ошибка 33: Документ не является деталью

print (kompas_check())
if kompas_check() != True:
    exit(32)


api5, api7, kompas_document, kompas_object, application, kompas_document_3d = connectAPI()
main_lfn()

part7 = kompas_document_3d.TopPart
propertyMng = api7.IPropertyMng(application)
propertyKeeper = api7.IPropertyKeeper(part7)


def set_property(property_name, value):
    i = 0
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



#Дописать проверку на уже заполненную БЧ деталь
#Дописать сохранение состояния и откат к не_БЧ детали
#Дописать обработчик допусков
#Дописать обработчик Квалитетов


#Проверка, является ли файл деталью
if kompas_document.DocumentType != 4:
    application.MessageBoxEx("Данный макрос работает только с деталью", "Документ не является деталью", 0)
    exit(33)

root = Tk()
root.title("Приложение на Tkinter")
root.geometry("300x250")
label = Label(text="Создание БЧ детали")
label.pack()
root.mainloop()

print(smartRound(get_property_value("Масса")))

'''bche_name = get_property_value("Наименование") + "@/" + get_property_value("Материал") + "@/" + "L = 100$m+0,8;-1$"
#if Bch_Name
set_property("Форматы листов документа", "БЧ")
set_property("Наименование", bche_name)
set_property("Примечание", smartRound(get_property_value("Масса")))'''
