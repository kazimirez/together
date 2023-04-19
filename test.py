
def to_drawing(s=""):
    i = s.find("@")
    if s.find("@") == -1:
        return s
    s = s[:i]
    return s

if __name__ == '__main__':
    print(to_drawing("Деталь закаленная @/ Труба по ГОСТ 1111 @/ L = 55"))
    print(to_drawing("Деталь закаленная"))
    print(to_drawing("Деталь"))
    print(to_drawing("Деталь@/ L = 55"))
    print(to_drawing("1"))