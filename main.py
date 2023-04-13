
from leafan import *

api5, api7, kompas_document, kompas_object, application, kompas_document_3d = connectAPI()
main_lfn()


part7 = kompas_document_3d.TopPart
propertyMng = api7.IPropertyMng(application)
propertyKeeper = api7.IPropertyKeeper(part7)


def findProperty (propertyName, value):
    i = 0
    for i in range (propertyMng.PropertyCount(kompas_document)):
        property = propertyMng.GetProperty(kompas_document, i)
        propertyVal = propertyKeeper.GetPropertyValue(property, "", True, True)
        print('\nИмя свойства: ', property.Name, '\nId свойства: ', property.Id, '\nЗначение свойства: ', propertyVal[1])
        if property.Name == propertyName:
            propertyKeeper.SetPropertyValue(property, value, True)
            print(propertyVal[1])
            return property
        i += 1
# Выбрать свойство
# Установить значение
findProperty("Форматы листов документа", "БЧ")