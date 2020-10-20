# Магические методы __getitem__, __setitem__, __delitem__

class Vector0:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        print("__repr__ called")
        return str(self.values)

v1 = Vector0(1, 2, 434, 32)
print(f'v1: {v1}')                      # неявный вызов метода __repr__
print('----------------------------------------')

v2 = Vector0(3, 43, 5, 56, 45, 3423)
print(f'v2: {v2}')                      # неявный вызов метода __repr__
print('----------------------------------------')

try:
    print(v2[1])                        # Выдаст ошибку TypeError, потому что экземпляры не поддерживают операцию индексирования
except TypeError as te:
    print(te)
print('----------------------------------------')



class Vector00:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        print("__repr__ called")
        return str(self.values)

    # добавляет функционал операции индексирования
    def __getitem__(self, item):
        print("__get_item__ called")
        return self.values[item]

v3 = Vector00(34, 85, 1431, 463)
print(v3[3])
try:
    print(v3[12])                       # Выдаст ошибку IndexError из-за выхода за пределы списка
except IndexError as ie:
    print(ie)
try:
    print(v3['ewd'])                    # Выдаст ошибку TypeError, потому что нельзя сравнивать число со строкой
except TypeError as te:
    print(te)
try:
    v3[2] = 54                          # Выдаст TypeError, потому что класс объекта не поддерживает операцию изменения
except TypeError as te:
    print(te)
print('----------------------------------------')



class Vector000:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        print("__repr__ called")
        return str(self.values)

    # добавляет функционал операции индексирования
    def __getitem__(self, item):
        print("__get_item__ called")
        if isinstance(item, int):
            if 0 <= item < len(self.values):
                return self.values[item]
            else:
                #raise IndexError("Индекс за границами коллекции")
                return None
        else:
            return None

    # добавляет функционал установки значения по индексу
    def __setitem__(self, key, value):
        print("__set_item__ called")
        if isinstance(key, int):
            if 0 <= key < len(self.values):
                self.values[key] = value


v4 = Vector000(48, 855, 11, 463, 77)
print(f'v4[3] = {v4[3]}')
print(f'v4[17] = {v4[17]}')             # Индекс за пределами списка, вернёт None
print(f"v4['qwr'] = {v4['qwr']}")       # Индекс не тип int, вернёт None
v4[2] = 22                              # Неявный вызов __setitem__
print(f'v4[2] = {v4[2]}')
v4[17] = 1233                           # Неявный вызов __setitem__, ничего не произойдёт, потому, что индекс за пределами списка
print(f'v4[17] = {v4[17]}')             # Индекс за пределами списка, вернёт None
print('----------------------------------------')

try:
    del v4[3]                           # Выдаст ошибку AttributeError, поскольку методе __delitem__ не переопределён
except AttributeError as ae:
    print("Не определён метод: ", ae)
print('----------------------------------------')



class Vector0000:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        print("__repr__ called")
        return str(self.values)

    # добавляет функционал операции индексирования
    def __getitem__(self, item):
        print("__getitem__ called")
        if isinstance(item, int):
            if 0 <= item < len(self.values):
                return self.values[item]
            else:
                #raise IndexError("Индекс за границами коллекции")
                return None
        else:
            return None

    # добавляет функционал установки значения по индексу
    def __setitem__(self, key, value):
        print("__setitem__ called")
        if isinstance(key, int):
            if 0 <= key < len(self.values):
                self.values[key] = value

    # добавляет функционал удаления элемента в экземпляре
    def __delitem__(self, key):
        print("__delitem__ called")
        if isinstance(key, int):
            if 0 <= key < len(self.values):
                del self.values[key]

v5 = Vector0000(324, 646, 78, 132)
del v5[1]
print(v5)
print('----------------------------------------')



# Переопределим __setitem__ для возможности создания разрежённого списка
# Переопределим __getitem__ для нумерации списка с 1-цы
class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        print("__repr__ called")
        return str(self.values)

    # добавляет функционал операции индексирования
    def __getitem__(self, item):
        print("__getitem__ called")
        if isinstance(item, int):
            if 1 <= item <= len(self.values):
                return self.values[item - 1]
            else:
                #raise IndexError("Индекс за границами коллекции")
                return None
        else:
            return None

    # добавляет функционал установки значения по индексу
    def __setitem__(self, key, value):
        print("__setitem__ called")
        if isinstance(key, int):
            if 1 <= key <= len(self.values):
                self.values[key - 1] = value
            elif key > len(self.values):
                diff = key - len(self.values)
                self.values.extend([None] * diff)
                self.values[key - 1] = value

    # добавляет функционал удаления элемента в экземпляре
    def __delitem__(self, key):
        print("__delitem__ called")
        if isinstance(key, int):
            if 0 <= key < len(self.values):
                del self.values[key]

v6 = Vector(34, 606, 80, 14132, 89)
print(f'v6[3] = {v6[3]}')               # неявный вызов __getitem__, получим 80 (3-й элемент списка, нумерация с 1-цы)
print(f'v6[12] = {v6[12]}')
print('----------------------------------------')
print(v6)
v6[14] = 776                            # неявный вызов __setitem__, список расширится до нужной длины
print(v6)
print('----------------------------------------')
