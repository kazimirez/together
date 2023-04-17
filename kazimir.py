def replacer(number):
    return str(number).replace('.', ',')

#Знаешь как это ломает программу?
if __name__ == '__main__':
    inputnumber = input("enter a number: ")
    b = replacer(inputnumber)
    print(b)

up = input()
low = input()
grade = input()


class Dimension:
    def __init__(self, dim):
        self.dim = dim
        self.upper_deviation = up
        self.lower_deviation = low
        self.it_grade = grade
        self.upper_deviation_sign = '+'
        self.lower_deviation_sign = '-'


    def print_dim(self):
        x = str(self.dim)
        return x

    def print_it_grade(self):
        x = str(self.it_grade)
        return x

    def print_tolerance(self):
        if self.upper_deviation == self.lower_deviation and self.upper_deviation != None:
            x, y = str(self.upper_deviation), str(self.lower_deviation)
            return "\u00B1" + x
        elif self.upper_deviation != self.lower_deviation:
            x, y = str(self.upper_deviation), str(self.lower_deviation)
            return "$m" + x + ";" + y + "$"


dim1 = Dimension(50)

dim1.upper_deviation = 2
dim1.lower_deviation = 1
dim1.it_grade = None
print(dim1.print_dim(), dim1.print_tolerance(), sep="")
