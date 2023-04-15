from leafan import *
#from kazimir import replacer

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


print(smartRound(get_property_value("Масса")))


#Дописать проверку на то, что модель является деталью
#Дописать проверку на уже заполненную БЧ деталь
#Дописать сохранение состояния и откат к не_БЧ детали
#Дописать обработчик допусков
#Дописать обработчик Квалитетов
bche_name = get_property_value("Наименование") + "@/" + get_property_value("Материал") + "@/" + "L = 100$m+0,8;-1$"
#if Bch_Name
set_property("Форматы листов документа", "БЧ")
set_property("Наименование", bche_name)
set_property("Примечание", smartRound(get_property_value("Масса")))
