# Атрибуты класса

class Person:
    name = 'Ivan'
    age = 30

print(Person)                       # Обращение к классу
print()

print(Person.name)                  # Обращение к атрибуту name класса Person
print(Person.age)                   # Обращение к атрибуту age класса Person
#print(Person.x)                    # Обращение к несуществующему атрибуту класса вызовет ошибку AttributeError
print()

print(Person.__dict__)              # Получить атрибуты класса (в виде mappingproxy)
print(getattr(Person, 'name'))      # Обращение к атрибуту name класса Person
#print(getattr(Person, 'x'))        # Обращение к несуществующему атрибуту класса вызовет ошибку AttributeError
print(getattr(Person, 'x', 100))    # Обращение к атрибуту класса с указанием значения по умолчанию в случае отсутствия
print(getattr(Person, 'name', 200)) # Обращение к атрибуту класса с указанием значения по умолчанию в случае отсутствия
print()

Person.name = 'Misha'               # Изменение значения атрибута name класса Person
print(Person.name)
Person.x = 100                      # Динамическое создание атрибута x в классе Person
print(Person.__dict__)
print(Person.x)
Person.x = [1, 2, 3]                # Изменение значения атрибута x класса Person
print(Person.__dict__)
print(Person.x)
print()

setattr(Person,'x', 200)            # Изменение значения атрибута x класса Person
print(Person.x)
setattr(Person,'y', 10)             # Динамическое создание атрибута
print(Person.__dict__)
print(Person.y)
print()

del Person.x                        # Динамическое удаление атрибута класс
print(Person.__dict__)
print()
#del Person.k                       # Удаление несуществуюшего атрибута класса вызовет ошибку AttributeError

delattr(Person, 'y')                # Динамическое удаление атрибута класса
print(Person.__dict__)
print()

a = Person()
b = Person()

Person.z = 100                      # Динамическое создание атрибута класса влияет на все существующие объекты данного класса
print(a.z)
print(b.z)

del Person.age                      # Динамическое удаление атрибута класса влияет на все существующие объекты данного класса
#print(a.age)                       # Вызовет ошибку AttributeError
#print(b.age)                       # Вызовет ошибку AttributeError

Person.name = 'Misha'               # Изменение значения атрибута класса влияет на все существующие объекты данного класса
print(a.name)
print(b.name)

a.b = 200                           # Добавление атрибута объекта коснётся только этого объекта
print(a.b)
#print(b.b)                         # Вызовет ошибку AttributeError
