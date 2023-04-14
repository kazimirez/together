def replacer(number):
    return str(number).replace('.', ',')


inputnumber = input("enter a number: ")
b = replacer(inputnumber)
print(b)

