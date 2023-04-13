import pythoncom
from win32com.client import Dispatch, gencache, VARIANT

def main_lfn():
    print('\nLeafan main start!')

#Функция от пользователя из телеграм чатика. выводит свойства деталей
'''def PrintPropetyValue(part) -> None:
    property_keeper = kompas_api7_module.IPropertyKeeper(part)
    for property_index in range(property_count):
        property = property_mng.GetProperty(kompas_document, property_index)
        value, base_unit, from_source = "", True, True
        result, value, from_source = property_keeper.GetPropertyValue(property, value, base_unit, from_source)
        print(property.Name, value)
        if property_keeper.IsComplexPropertyValue(property):
            value1, from_source = property_keeper.GetComplexPropertyValue(property, from_source)
            print(property.Name, value1)'''



def connectAPI():

    #  Подключим константы API Компас
    constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
    constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

    #  Подключим описание интерфейсов API5
    api5 = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
    kompas_object = api5.KompasObject(
        Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(api5.KompasObject.CLSID, pythoncom.IID_IDispatch))

    #  Подключим описание интерфейсов API7
    api7 = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
    application = api7.IApplication(
        Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(api7.IApplication.CLSID, pythoncom.IID_IDispatch))

    #  Получим активный документ
    kompas_document = application.ActiveDocument  # Указатель на текущий документ
    kompas_document_3d = api7.IKompasDocument3D(kompas_document)
    iDocument3D = kompas_object.ActiveDocument3D()

    return api5, api7, kompas_document, kompas_object, application, kompas_document_3d