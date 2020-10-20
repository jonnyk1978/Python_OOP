# Наследование. Расширение (extending)

class Person:

    def breathe(self):
        print('Человек дышит')

# класс Doctor расширяет (extend) класс Person
class Doctor(Person):

    # расширение (extending)
    def sleep(self):
        print('Доктор спит')

d = Doctor()
d.sleep()

p = Person()
try:
    p.sleep()               # объект класса Person не имеет такого поведения, поэтому выдаст ошибку AttributeError
except AttributeError as ae:
    print(ae)

# метод breathe доступен обоим объектам (и класса Person, и класса Doctor)
d.breathe()
p.breathe()
print('-------------------------------------------------------------------------------')

#-------------------------------------------------------------------------------

class Person:

    def breathe(self):
        print('Человек дышит')

# класс Doctor расширяет (extend) класс Person
class Doctor(Person):

    # расширение (extending)
    def sleep(self):
        print('Доктор спит')

    # переопределение (overriding)
    def breathe(self):
        print('Доктор дышит')

d = Doctor()
p = Person()

d.breathe()
p.breathe()
print('-------------------------------------------------------------------------------')

#-------------------------------------------------------------------------------

