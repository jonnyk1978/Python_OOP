# "__Магические методы__ (__init__)"

class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('Hello, new object is ', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


print(Cat.__dict__)
print()
tom = Cat('Tom', 'siam', 40, 'black')   # Создаём экземпляр tom класса Cat (в консоли получим надпись 'Hello...' из-за автоматического вызова метода __init__)
print(tom.__dict__)
print()
jerry = Cat('Jerry')                    # __init__ вызывается при создании каждого экземпляра класса
print(jerry.__dict__)
print()
kelly = Cat('Kelly', age=40)
print(kelly.__dict__)
print()

