import pythoncom
import psutil
from win32com.client import Dispatch, gencache, VARIANT
from kazimir import replacer

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


class Breckets:
    def __init__(self, string):
        self.flag = False
        self.string = string

    def get_in_breckets(self):
        if self.flag == False:
            self.flag = True
            self.string = "(" + self.string + ")"
            return self.string
        return self.string
    def in_breckets(self):
        return self.flag


#Класс который описывает размер, допуски квалитеты. И возвращает строку с написанным размером для записи в Наименовании Компас 3D
class Dimension:
    def __init__(self, dim):
        self.dim = dim
        self.upper_deviation = None
        self.lower_deviation = None
        self.it_grade = ''
        self.upper_deviation_sign = "+"
        self.lower_deviation_sign = "-"

    def print_dim(self):
        x = str(self.dim)
        return x

    def print_it_grade(self):
        x = str(self.it_grade)
        return x

    def print_tolerance(self, flag_it="True", flag_diviation="True"):
        #Проверка, если один из допусков равен 0, то он не будет писаться
        if self.upper_deviation == 0:
            self.upper_deviation_sign = ""
            self.upper_deviation = ""
        if self.lower_deviation == 0:
            self.lower_deviation_sign = ""
            self.lower_deviation = ""

        first = str(self.dim)
        second = str(self.it_grade)

        #Скрываются ненужные значения квалитета
        if not flag_it:
            second = ""

        #Выбор типа написания, в одну строчку или два разных значения
        third = Breckets("$m" + str(self.upper_deviation_sign) + str(self.upper_deviation) + ";" + str(self.lower_deviation_sign) + str(self.lower_deviation) + "$")
        if self.upper_deviation == self.lower_deviation and self.upper_deviation != 0:
            if self.upper_deviation_sign != self.lower_deviation_sign:
                third.string = "\u00B1" + str(self.upper_deviation)

        # Скрываются ненужные значения допуска
        if not flag_diviation:
            third.string = ""

        #Заключение в скобки при необходимости
        if flag_diviation == flag_it == True and second != "":
            third.get_in_breckets()

        #print(third.in_breckets())
        all = first+second+third.string
        return (all)


def breckets(string):
    return "(" + string + ")"


#"\u00B1"
x = Dimension(23)
x.upper_deviation = 1
x.lower_deviation = 0.2
x.it_grade = "m8"
print(x.print_tolerance(True, True))


def smartRound(part_mass):
    if part_mass < 0.1:
        part_mass *= 1000
        return replacer(round(part_mass, 1)) + " г"
    elif 0.1 <= part_mass <= 10:
        return replacer(round(part_mass, 2)) + " кг"
    elif 10 <= part_mass <= 100:
        return replacer(round(part_mass, 1)) + " кг"
    else:
        return replacer(round(part_mass, 0)) + " кг"

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


def kompas_check():
    for proc in psutil.process_iter():
        name = proc.name()
        #print(name)
        if name == "KOMPAS.Exe" or "KOMPAS.exe":
            return True
    return False