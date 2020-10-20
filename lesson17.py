# Магические методы __add__, __mul__, __sub__, __truediv__

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

b = BankAccount('Ivan', 900)
print(b.balance)
print(b.balance + 400)
try:
    print(b + 700)                  # Вызовет ошибку TypeError (нельзя складывать BankAccount и int)
except TypeError as te:
    print(te)
try:
    print(b + 'Ivanov')             # Вызовет ошибку TypeError (нельзя складывать BankAccount и str)
except TypeError as te:
    print(te)
print('------------------------------------------------------')


class BankAccount2():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')

        # если второй аргумент BankAccount
        if isinstance(other, BankAccount2):
            return self.balance + other.balance

        # если второй аргумент int или float
        if isinstance(other, (int, float)):
            return self.balance + other

        # если ничего не подошло, генерируем исключение
        raise NotImplemented


r = BankAccount2('Misha', 78)
print(r + 12)                       # Ошибки нет
print(r + 135.543)                  # Ошибки нет
s = BankAccount2('Tanya', 900)
print(r + s)                        # Ошибки нет

try:
    print(r + 'AFaskojg')           # Выдаст ошибку NotImplemented, которую мы сами генериурем, в случае неподходящих аргументов
except TypeError as te:
    print(te)

try:
    print(12 + r)                   # Выдаст TypeError, интерператор пытается вызвать метод __add__ у 12 (12.__add()__)
except TypeError as te:
    print(te)

try:
    print((12).__add__(r))          # Выдаст TypeError, поскольку это аналог предыдущей записи
                                    # На это интерпретатор не останавливается и он меняет аргументы местами
                                    # и вызывает метод _radd__, который можно реализовать
except TypeError as te:
    print(te)

print('------------------------------------------------------')


# добавим метод __radd__
class BankAccount3():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')

        # если второй аргумент BankAccount
        if isinstance(other, BankAccount2):
            return self.balance + other.balance

        # если второй аргумент int или float
        if isinstance(other, (int, float)):
            return self.balance + other

        # если ничего не подошло, генерируем исключение
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ called')
        return self + other

    def __mul__(self, other):
        print('__mul__ called')

        # если второй аргумент BankAccount
        if isinstance(other, BankAccount2):
            return self.balance * other.balance

        # если второй аргумент int или float
        if isinstance(other, (int, float)):
            return self.balance * other

        # если второй аргумент str
        if isinstance(other, str):
            return self.name + other

        # если ничего не подошло, генерируем исключение
        raise NotImplemented

r = BankAccount3('Misha', 78)
print(12 + r)   # Ошибки больше нет, сначала вызывается метод __radd__, а затем метод __add__ из-за + в методе __radd__
print(r * 3)    # Вызывается метод __mul__
print(r * 'ttt')# Вызывается метод __mul__

print('------------------------------------------------------')
