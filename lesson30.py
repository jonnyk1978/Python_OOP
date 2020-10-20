# Множественное наследование

class Doctor:

    def can_cure(self):
        print('Я доктор, я умею лечить')

class Builder:

    def can_build(self):
        print('Я строитель, я умею строить')

class Person(Doctor, Builder):
    pass

s = Person()
s.can_build()
s.can_cure()
print('--------------------------------------------------------------------')
#--------------------------------------------------------------------

class Doctor:

    def can_cure(self):
        print('Я доктор, я умею лечить')

class Builder:

    def can_build(self):
        print('Я строитель, я умею строить')

class Person(Doctor, Builder):
    def can_build(self):
        print('Я человек, я тоже умею строить')

s = Person()
s.can_build()
print('--------------------------------------------------------------------')

#--------------------------------------------------------------------

class Doctor:

    def can_cure(self):
        print('Я доктор, я умею лечить')
    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')

class Builder:

    def can_build(self):
        print('Я строитель, я умею строить')

class Person1(Doctor, Builder):         # порядок перечисления важен, он задаёт порядок поиска имён переменных и методов,
                                        # не определённых в родном классе (MRO - Method Resolution Order)
    pass

class Person2(Builder, Doctor):         # порядок перечисления важен, он задаёт порядок поиска имён переменных и методов,
                                        # не определённых в родном классе (MRO - Method Resolution Order)
    pass

s = Person1()
t = Person2()
s.can_build()                       # вызовет метод can_build у из класса Doctor
t.can_build()                       # вызовет метод can_build у из класса Builder
print()
print(Person1.__mro__)              # выводит последовательность наследования
print(Person2.__mro__)              # выводит последовательность наследования
print('--------------------------------------------------------------------')

#--------------------------------------------------------------------

class Doctor:

    def graduate(self):
        print('Ура, я отучился на доктора')
    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')

class Builder:

    def graduate(self):
        print('Ура, я отучился на строителя')

    def can_build(self):
        print('Я строитель, я умею строить')

class Person(Doctor, Builder):

    def graduate(self):
        print('Посмотрим, кем я стал?')
        super().graduate()                  # вызовет метод graduate() у класса Doctor, поскольку он первый в порядке наследования
        Builder.graduate(self)              # вызовет метод graduate() у класса Builder

p = Person()
p.graduate()
print(Person.__mro__)                       # выводит последовательность наследования
print('--------------------------------------------------------------------')

#--------------------------------------------------------------------

class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')
    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')

class Builder:

    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ура, я отучился на строителя')

    def can_build(self):
        print('Я строитель, я умею строить')

class Person1(Builder, Doctor):

    def __init__(self, rank, degree):
        self.rank = rank
        self.degree = degree

    def __str__(self):
        return f" Person {self.rank} {self.degree}"

class Person2(Builder, Doctor):

    def __init__(self, rank, degree):
        super().__init__(rank)              # Делегирование
        Doctor.__init__(self, degree)       # Делегирование

    def __str__(self):
        return f" Person {self.rank} {self.degree}"

p1 = Person1(5, 'spec')
p2 = Person2(3, 'ass')
print(p1)
print(p2)
print('--------------------------------------------------------------------')
