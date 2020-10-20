# Наследование. Делегирование (delegating)
# Функция super()

class Person:

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    def breathe(self):
        print('Доктор дышит')


p = Person()
d = Doctor()

p.breathe()
d.breathe()
print('--------------------------------------------------------')

# Иногда требуется вызвать метод, который уже переопределён в своём классе, из родительского класса
class Person:

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    def breathe(self):
        print('Доктор дышит')
        super().breathe()       # принудительный вызов метода, определённого выше по иерархи (в одном из родительских классов)


p = Person()
d = Doctor()
d.breathe()                     # вызовется метод breathe() из Doctor, который в свою очередь вызовет breathe() из Person
print('--------------------------------------------------------')

# Область применения вызова уже переопределённых методов выше по иерархии
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Person {self.name} {self.surname}"

    def info(self):
        print('Parent class')
        print(self)

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f"Doctor {self.name} {self.surname}"

    def breathe(self):
        print('Доктор дышит')
        super().breathe()       # принудительный вызов метода, определённого выше по иерархи (в одном из родительских классов)


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 29)

print(p.name, p.surname)
print(d.name, d.surname, d.age)
print('--------------------------------------------------------')

# вызовется метод info(), унаследованный от родительского класса,
# в который будет передан экземпляр класса Doctor,
# поэтому print(self) неявно вызовет метод __str__ из класса Doctor, а не Person
d.info()
print('--------------------------------------------------------')
p.info()
print('--------------------------------------------------------')
