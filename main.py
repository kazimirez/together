from leafan import *
from kazimir import *

api5, api7, kompas_document, kompas_object, application, kompas_document_3d = connectAPI()
main_lfn()

part7 = kompas_document_3d.TopPart
propertyMng = api7.IPropertyMng(application)
propertyKeeper = api7.IPropertyKeeper(part7)


def setProperty(propertyName, value):
    i = 0
    for i in range(propertyMng.PropertyCount(kompas_document)):
        property = propertyMng.GetProperty(kompas_document, i)
        if property.Name == propertyName:
            propertyKeeper.SetPropertyValue(property, value, True)
            return property
        i += 1


def getPropertyValue(propertyName):
    i = 0
    for i in range(propertyMng.PropertyCount(kompas_document)):
        property = propertyMng.GetProperty(kompas_document, i)
        if property.Name == propertyName:
            propertyVal = propertyKeeper.GetPropertyValue(property, "", True, True)
            return propertyVal[1]


def smartRound(part_mass):
    if part_mass < 0.1:
        part_mass *= 1000
        return replacer(round(part_mass, 1)) + " г"
    elif 0.1 <= part_mass <= 10:
        return replacer(round(part_mass, 2)) + " кг"
    elif 10 <= part_mass <= 100:
        return replacer(round(part_mass, 1)) + " кг"
    else:
        return replacer(str(round(part_mass, 0)) + " кг")

print(smartRound(getPropertyValue("Масса")))

#Дописать проверку на уже заполненную БЧ деталь
'''Bch_Name = getPropertyValue ("Наименование") + "@/" + getPropertyValue ("Материал") + "@/" + "L = $m;$"
if Bch_Name 
    setProperty("Форматы листов документа", "БЧ")
    setProperty("Наименование", Bch_Name)
    setProperty("Примечание", smartRound(getPropertyValue("Масса")))'''
