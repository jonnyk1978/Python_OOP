# Наследование. Введение

class Doctor0:

    def can_walk(self):
        print('Я могу ходить')

    def can_cure(self):
        print('Я могу лечить')

class Architect0:
    def can_walk(self):
        print('Я могу ходить')

    def can_build(self):
        print('Я могу построить здание')

d = Doctor0()
d.can_cure()

a = Architect0()
a.can_build()
try:
    a.can_cure()                # Вызовет ошибку AttributeError, потому что экземпляр класса Architect
                                # не имеет метода can_cure, а про внутренности класса Doctor он ничего не знает
except AttributeError as ae:
    print(ae)

# метод can_walk есть у обоих экземпляров, поэтому ошибки не будет
# но здесь у нас получается дублирование кода
a.can_walk()
d.can_walk()
print('-------------------------------------------')



# Для избавления от дублирования, схожее поведение можно объединить в родительском (базовом) классе
# родительский (parent) класс
class Person:
    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')

# подкласс (subclass) класса Person
# класс Doctor расширяет (extend) класс Person
class Doctor(Person):
    def can_cure(self):
        print('Я могу лечить')

# подкласс (subclass) класса Person
class Architect(Person):
    def can_build(self):
        print('Я могу построить здание')

a = Architect()
d = Doctor()

# данные методы не описаны в классах экземпляров a и d, они берутся (наследуются) из базового (родительского) класса
a.can_walk()
d.can_walk()
a.can_breathe()
d.can_breathe()
print('-------------------------------------------')

print('Doctor is subclass of Person - ', issubclass(Doctor, Person))           # Проверяет является ли класс Doctor подклассом класса Person
print('Person is subclass of Doctor - ', issubclass(Person, Doctor))
print('-------------------------------------------')
print('d is instance of Doctor - ', isinstance(d, Doctor))  # Является ли экземпляр d экземпляром класса Doctor
print('d is instance of parent class Person - ', isinstance(d, Person))  # Является ли экземпляр d экземпляром родительского класса Person
print('-------------------------------------------')



# Создадим класс Ortoped, расширяющий класс Doctor
# Он унаследует все атрибуты классов, стоящих выше по иерархии (и Doctor, и Person)
class Ortoped(Doctor):
    pass

o = Ortoped()
o.can_walk()        # Person
o.can_breathe()     # Person
o.can_cure()        # Doctor
print('-------------------------------------------')

