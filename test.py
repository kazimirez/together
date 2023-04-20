string = "1"



def set_upper_deviation(string):  # Надо исправить, если приходит пустая строка, то выдает ошибку
    if len(string) > 0:
        if string[0] == "+" or string[0] == "-":
            return string[0] + string[1:]
        elif string == "0":
            return "" + "0"
        else:
            return "+" + string
    return "Пустая строка"



print(set_upper_deviation(string))

print(string[0] == "+" or string[0] == "-")