# Магические методы __iter__, __next__

# Вынесем оценки в свой собственный класс

class Mark:
    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('__next__ Mark called')
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter

class Student0:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

igor = Student0('Igor', 'Nikolaev', [3, 4, 5, 6, 3])

# Выдаст ошибку 'Student0' object is not iterable
try:
    for i in igor:
        print(i)
except TypeError as te:
    print(te)
print('---------------------------------------------------------------')

# обычные списки итерабельны
a = [1, 2, 3]       # список
b = iter(a)         # получаем итератор (коллекция, элементы которой можно поочерёдно обойти)
print(a)
print(b)
# обход списка
print(next(b))
print(next(b))
print(next(b))
try:
    print(next(b))      # получим ошибку StopIteration
except StopIteration as si:
    print('Stop Iteration')
print('---------------------------------------------------------------')

# итератор, это коллекция, которую можно обойти только один раз
# чтобы пройти вновь, нужно создать новый итератор
# сделать это можно с помощью магического метода __iter__
c = a.__iter__()
print(c)
print(c.__next__())
print(c.__next__())
print(c.__next__())
try:
    print(c.__next__())
except StopIteration as si:
    print('Stop Iteration')
print('---------------------------------------------------------------')



# Первый вариант сделать класс итерабельным
class Student00:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

andrey = Student00('Andrey', 'Vasil\'ev', [5, 5, 9, 6, 2])
for i in andrey:
    print(i)
print('---------------------------------------------------------------')



# Основной вариант сделать класс итерабельным
class Student000:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    # при итерации будет вызываться именно этот метод
    # недостаток: возвращается итератор от экземпляра типа str
    # а нам хочется итерировать сам экземпляр
    def __iter__(self):
        print('call iter')
        return iter(self.name)

vasyan = Student000('Vasiliy', 'Petrovich', [3, 4, 4, 7, 1])
# неявный вызов метода __iter__
for i in vasyan:
    print(i)
print('---------------------------------------------------------------')



class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    # при итерации будет вызываться именно этот метод
    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)         # возвращаем сам экземпляр

    # а здесь уже описываем логику возвращения, чтобы не выпадала ошибка TypeError: iter() returned non-iterator of type
    def __next__(self):
        print('__next__ Student called')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m = Mark([3, 4, 4, 7, 1])
petya = Student('Petr', 'Ivanovich', m)
# неявный вызов метода __iter__
for i in petya:
    print(i)
print('---------------------------------------------------------------')
