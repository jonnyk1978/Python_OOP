# Декоратор Property

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # геттер
    def get_balance(self):
        print('get balance')
        return self.__balance

    # сеттер
    def set_balance(self, value):
        print('set balance')
        print(value)
        # проверяем введённое значение баланса на корректность
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    # делитер
    def delete_balance(self):
        print('delete balance')
        del self.__balance

    ## зададим свойство
    #balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    # Переопределим использование property
    my_balance = property()             # создаём свойство
    my_balance = my_balance.getter(get_balance)     # вызываем у него геттер и передаём ему название нашего метода, результатом будет свойство
    my_balance = my_balance.setter(set_balance)     # вызываем у него геттер и передаём ему название нашего метода, результатом будет свойство
    my_balance = my_balance.deleter(delete_balance) # вызываем у него геттер и передаём ему название нашего метода, результатом будет свойство

# Посмотрим что такое property
x = property()
print(x.__dir__())              # методы getter, setter, deleter
print()
print(x.getter(90))             # попробуем вызвать один из них

a = BankAccount('Ivan', 100)
# Обращаемся через свойства
print('Обращаемся через свойства')
print(a.my_balance)
print()
a.my_balance = 1000
print(a.my_balance)
print('---------------------------------------------')



# В вышеописанном классе мы можем и вызывать методы напрямую, и обращаться к ним через свойства
# Попробуем избавиться от двойной функциональности
# геттеры, сеттеры и делитеры должны называться одинаково
class BankAccount2:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # геттер
    @property                       # означает my_balance = property(my_balance), т.е. декорирование метода
    def my_balance(self):
        print('get balance')
        return self.__balance

    # сеттер
    @my_balance.setter              # вызываем методе setter через декоратор (свойство my_balance)
    def my_balance(self, value):
        print('set balance')
        print(value)
        # проверяем введённое значение баланса на корректность
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    # делитер
    @my_balance.deleter             # вызываем методе deleter через декоратор (свойство my_balance)
    def my_balance(self):
        print('delete balance')
        del self.__balance

    ## зададим свойство
    #balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    # Переопределим использование property
    # my_balance = property(my_balance)               # декорируем метод my_balance свойством
    # my_balance = my_balance.setter(set_balance)     # вызываем у него геттер и передаём ему название нашего метода, результатом будет свойство
    # my_balance = my_balance.deleter(delete_balance) # вызываем у него геттер и передаём ему название нашего метода, результатом будет свойство

b = BankAccount2('Misha', 200)
print(b.my_balance)             # обращаемся к методу как к свойству
try:
    print(b.my_balance())           # напрямую к методу мы обратиться не можем, поскольку он задекорирован
except TypeError:
    print('напрямую к методу мы обратиться не можем, поскольку он задекорирован')
print('---------------------------------------------')
print()

p = BankAccount2('Tod', 900)
# сеттеры и геттеры пропали, к ним нельзя обратиться напрямую
# осталось только одно свойство с которым мы и работаем, как с атрибутом
print(p.my_balance)
p.my_balance = 901
print(p.my_balance)
del p.my_balance
try:
    print(p.my_balance)
except AttributeError:
    print('Такого атрибута не существует')
