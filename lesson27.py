# Наследование. Переопределение. Overriding

class Person0:           # parent

    name = 'Adam'

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идёт')

class Doctor0(Person0):   # subclass
    pass

p = Person0()
p.breathe()
p.walk()
print(p.name)
print('---------------------------------------')

d0 = Doctor0()
# всё поведение и атрибуты будут унаследованы от родительского класса
d0.breathe()
d0.walk()
print(d0.name)
print('---------------------------------------')

class Doctor00(Person0):   # subclass

    # переопределяем атрибут родительского класса
    name = 'Ivan'

    # переопределяем метод родительского класса
    def breathe(self):
        print('Доктор дышит')

d00 = Doctor00()
d00.breathe()       # вызовет переопределённый родительский метод из класса Doctor00
d00.walk()          # вызовет унаследованный метод из класса Person
print(d00.name)     # выведет переопределённый атрибут в классе Doctor00
print('---------------------------------------')



# Person не имеет родителя, а значит неявно наследуется от object
# в итоге иерархия выглядит как: object -> Person -> Doctor..
# Значит Person наследует магические методы класса object, такие как __init__, __str__ и т.д., которые тоже можно переопределить
class Person:           # parent

    def __init__(self, name):
        print('Person __init__ called')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идёт')

class Doctor(Person):   # subclass

    # переопределяем атрибут родительского класса
    name = 'Ivan'

    # переопределяем метод родительского класса
    def breathe(self):
        print('Доктор дышит')

    # переопределим метод __str__
    def __str__(self):
        return f"Doctor {self.name}"

d = Doctor('John')          # вызовется метод __init__ класса Person, который унаследован от родительского класса Person
                            # но не переопределён в классе Doctor
p = Person('Adam')          # вызовется метод __init__ класса Person
print(p.name, d.name)
print('---------------------------------------')
print(p, d)                 # к 'p' применится метод __str__, унаследованный от object
                            # к 'd' применится метод __str__, переопределённый в самом классе Doctor
print('---------------------------------------')



class Person:           # parent

    def __init__(self, name):
        print('Person __init__ called')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идёт')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    # переопределим метод __str__
    def __str__(self):
        return f"Person {self.name}"

class Doctor(Person):   # subclass

    # переопределяем атрибут родительского класса
    name = 'Ivan'

    # переопределяем метод родительского класса
    def breathe(self):
        print('Доктор дышит')

    # переопределим метод __str__
    def __str__(self):
        return f"Doctor {self.name}"

d = Doctor('John')          # вызовется метод __init__ класса Person, который унаследован от родительского класса Person
                            # но не переопределён в классе Doctor
p = Person('Adam')          # вызовется метод __init__ класса Person
print(p, d)                 # к 'p' применится метод __str__, переопределённый в классе Person
                            # к 'd' применится метод __str__, переопределённый в классе Doctor
print('---------------------------------------')
# все три метода, спрятанные в методе combo, будут вызвана из экземпляра класса Person
p.combo()
print('---------------------------------------')
# методы, не переопределённые в классе Doctor, но спрятанные в унаследованном методе combo, будут вызвана из класса Person,
# а переопределённый метод breathe будет вызван из класса Doctor
d.combo()
print('---------------------------------------')

