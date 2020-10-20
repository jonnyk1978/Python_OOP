# Класс-методы (classmethod) и Статик-методы (stathicmethod)

# Проблема
class Example:
    def hello():
        print('hello')

Example.hello()         # Ошибки не будет
p = Example()
try:
    p.hello()           # Выдаст ошибку TypeError, потому что в метод неявно передаётся экземпляр класса,
                        # однако в аргументах метода нет принимаемых аргументов
except TypeError:
    print('Метод hello() не принимает аргументов')

print('--------------------------------------------')

# Решение проблемы (разные методы для класса и для экземпляра)
class Example2:
    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance hello {self}')

q = Example2()
q.instance_hello()
try:
    Example2.instance_hello()   # Выдаст ошибку TypeError, потому что метод instance_hello требует аргумент, который в данном
                                # случае не передаётся, посколько вызов идёт от имени класса
except TypeError:
    print('Ошибка вызова, потому что метод instance_hello требует аргумент')

print('--------------------------------------------')

# Как создать функцию, которую можно вызывать и от имени класса, и от экзмепляра класса?
# объявляем её staticmethod (лепим декоратор)
class Example3:
    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

Example3.static_hello()         # Ошибки нет
r = Example3()
r.static_hello()                # Ошибки нет

print('--------------------------------------------')

class Example4:
    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    # class-методы используются для вызова от экземпляра, но для возможности работы со всем классом
    @classmethod
    def class_hello(cls):
        print(f'class hello {cls}')

Example4.class_hello()  # Ошибки нет
s = Example4()
print(s.__class__)      # Интерпретатор сам определяет к какому классу принадлежит экземпляр и передаёт его в качестве аргумента class-методу
s.class_hello()         # Ошибки нет
