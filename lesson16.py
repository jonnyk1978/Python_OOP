# Магические методы __len__ (срабатывает при вызове функции len()) и __abs__(срабатывает при вызове функции abs())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Не все объекты поддерживают функцию len()
print(len('hfd90a8f'))          # Вернёт 8
print(len([1, 56, '6']))        # Вернёт 3
try:
    print(len(78))              # Вызовет ошибку TypeError
except TypeError as te:
    print('Нельзя применить функцию len() к числовому типу ' + te.__repr__())

a = Person('aoiuow', 'sdgfas')
try:
    print(len(a))               # Вызовет ошибку TypeError
except TypeError as te:
    print('Нельзя применить функцию len() к экземпляру ' + te.__repr__())
print('--------------------------------------')

# Не все объекты поддерживают функцию abs()
print(abs(-45.7))               # Вернёт 45.7
try:
    print(abs([1, 56, -9]))     # Вызовет ошибку TypeError
except TypeError as te:
    print('Нельзя применить функцию abs() к списку ' + te.__repr__())
try:
    print(abs('asgsa'))         # Вызовет ошибку TypeError
except TypeError as te:
    print('Нельзя применить функцию abs() к строковому типу ' + te.__repr__())
print('--------------------------------------')


# Добавим dunder-метод __len()__
class Person2:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


b = Person2('kiasudg', 'saowi')
print(len(b))                   # Применим функцию len() к экземпляру, неявно вызовется магический метод экземпляра __len()__, ошибки не будет
try:
    print(abs(b))               # Однако с abs() по-прежнему беда, TypeError
except TypeError as te:
    print('Нельзя применить функцию abs() к экземпляру ' + te.__repr__())
print('--------------------------------------')


class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return self.x2 - self.x1


t = Otrezok(5, 9)
print(len(t))
u = Otrezok(10, 9)              # Выдаст ошибку ValueError
try:
    print(len(u))
except ValueError as ve:
    print('Функция len() должна возвращать неотрицательное число ' + ve.__repr__())
print('--------------------------------------')


class Otrezok2:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)        # abs() вызывает метод __abs()__

    def __abs__(self):
        return abs(self.x2 - self.x1)


v = Otrezok2(8, 17)
print(len(v))
w = Otrezok2(16, 3)
print(len(w))                   # Теперь ошибки нет
print('--------------------------------------')


