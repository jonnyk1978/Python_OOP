# Функция как атрибут класса

class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod           # Декоратор, позволяющий вызывать функцию класса без self из экземпляра
    def drive():            # При таком определении функции (без self) её вызов возможен только через имя класса (Car.drive())
        print("Let's go")

print(Car.__dict__)
print()

Car.drive()                 # Вызов функции класса
getattr(Car, 'drive')()     # Вызов функции класса

a = Car()                   # Создаём экземпляр a класса Car
print(a.__dict__)
print(a.drive)              # Функция называется как bound method Car.drive
a.drive()                   # Вызовет ошибку TypeError если не указать декоратор @staticmethod
