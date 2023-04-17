def replacer(number):
    return str(number).replace('.', ',')

#Знаешь как это ломает программу?
if __name__ == '__main__':
    inputnumber = input("enter a number: ")
    b = replacer(inputnumber)
    print(b)

