# Уровни доступа к атрибутам и методам
# public, protected, private
#
# _ - protected (защищённый), рекомендательный уровень, уровень согласования между разработчиками,
# НЕ НУЖНО использовать данные атрибуты/методы вне самого класса
#
# __ - private (частный)
#
# Ни один уровень доступа НЕ даёт должной защиты. Для полной защиты нужно использовать модуль accessify,
# содержащий декораторы protected и private

class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    def print_protected_data(self):
        print(self._name, self._balance, self.__passport)

    def __print_private_data(self):
        print(self._name, self._balance, self.__passport)



account1 = BankAccount('Bob', 100000, 7826565283)
account1.print_protected_data()
print()
# доступ к protected-атрибутам есть, но пользоваться этим НЕ рекомендуется
# доступ к private-атрибутам вызовет ошибку AttributeError
print(account1._name)
print(account1._balance)
#print(account1.__passport)
print()

# доступ к приватным (инкапсулированным) атрибутам
#account1.__print_private_data()    # вызовет ошибку AttributeError
account1.print_public_data()        # вызов private-метода идёт через вызов public-метода
print()

print(dir(account1))
print()
account1._BankAccount__print_private_data()     # ещё один спосод вызова private-метода
print(account1._BankAccount__passport)          # и получения доступа к private-атрибуту
