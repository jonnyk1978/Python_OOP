# Наследование. Введение

class Person:
    pass

class Doctor(Person):
    pass

class Architect(Person):
    pass



# Любое значение в Python это объект
print(f'34 is object - {isinstance(34, object)}')
print(f'(3, 4) is object - {isinstance((3, 4), object)}')
print(f'int is object - {isinstance(int, object)}')
print(f'dict is object - {isinstance(dict, object)}')
print('--------------------------------------------------')

# Каждый встроенный тип является подклассом класса object
print(f'int is subclass of object - {issubclass(int, object)}')
print(f'dict is subclass of object - {issubclass(dict, object)}')
print('--------------------------------------------------')

# Каждый класс неявно является подклассом класса object
print(f'Person is subclass of object - {issubclass(Person, object)}')
print(f'Doctor is subclass of object - {issubclass(Doctor, object)}')
print(f'Architect is subclass of object - {issubclass(Architect, object)}')
print('--------------------------------------------------')

# А значит и каждый экземпляр созданного нами класса, является объектом класса object (наследует его)
a = Person()
print(f'a(Person) is istance of object - {isinstance(a, object)}')
print('--------------------------------------------------')

# Какие атрибуты имеет класс object
print(dir(object))
print('--------------------------------------------------')

# И каждый класс имеет те же атрибуты и поведение, поскольку является подклассом класса object
print(dir(Person))
print(a.__hash__())
print(a.__str__())
print(f'a == a ? - {a == a}')       # в том числе и сравнение (неявный вызов метода __eq__)
print('--------------------------------------------------')



class MyList(list):
    pass

t = MyList()
print(t)
# через экземпляр t мы увидим всё возможное поведение для списков (list)
t.append(2)
t.append(7)
t.append(-3)
print(t)
# Однако типом экземпляра t уже является класс MyList, а не сам list
print(type(t))
print(issubclass(MyList, list))
print(isinstance(t, MyList))
print(isinstance(t, list))
print(isinstance(t, object))
print('--------------------------------------------------')
