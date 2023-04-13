

import pythoncom
from leafan import *
from win32com.client import Dispatch, gencache, VARIANT
import LDefin2D
import MiscellaneousHelpers as MH

#  Подключим константы API Компас
constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

#  Подключим описание интерфейсов API5
api5 = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
kompas_object = api5.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(api5.KompasObject.CLSID,pythoncom.IID_IDispatch))

#  Подключим описание интерфейсов API7
api7 = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
application = api7.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(api7.IApplication.CLSID,pythoncom.IID_IDispatch))

#  Получим активный документ
kompas_document = application.ActiveDocument  # Указатель на текущий документ
kompas_document_3d = api7.IKompasDocument3D(kompas_document)
iDocument3D = kompas_object.ActiveDocument3D()



main_lfn()
part7 = kompas_document_3d.TopPart
propertyMng = api7.IPropertyMng(application)
propertyKeeper = api7.IPropertyKeeper(part7)


i = 0
for i in range (propertyMng.PropertyCount(kompas_document)):
    property = propertyMng.GetProperty(kompas_document, i)
    propertyVal = propertyKeeper.GetPropertyValue(property, "", True, True)
    print('\nИмя свойства: ', property.Name, '\nId свойства: ', property.Id, '\nЗначение свойства: ', propertyVal[1])
    if property.Name == "Форматы листов документа":
        propertyKeeper.SetPropertyValue(property, "БЧ", True)
        print(propertyVal[1])
        break
    i += 1
# Выбрать свойство
# Установить значение