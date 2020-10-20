# Моносостояние для всех экземпляров

class Cat:
    breed = 'pers'

# оба экземпляра имеют одинаковое значение атрибута breed при создании
a = Cat()
print(a.breed)
b = Cat()
print(b.breed)
print()

# изменение значения атрибута breed в экземпляре a, никак не влияет на значение этого атрибута в экземпляре b
a.breed = 'siam'
print(a.breed)
print(b.breed)
print()

# добавление атрибута в экземпляре b, также никак не влияет на содержимое экземпляра a
b.color = 'black'
print(a.__dict__)
print(b.__dict__)
print()

# Вновь создаваемый экземпляр примет атрибуты и их значения, описанные в классе. Экземпляры a и b никак не повлияют на экземпляр c
c = Cat()
print(c.__dict__)
print(c.breed)
print()

class Cat2:
    # Моносостояние
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat2.__shared_attr  # Каждый экземпляр при инициализации ссылается на один и тот же атрибут класса (словарь __shared_attr),
                                            # изменения в котором, соответственно, влияют на каждый экземпляр



d = Cat2()
f = Cat2()
g = Cat2()
print(d.__dict__)
print(f.__dict__)
print(g.__dict__)
print()
d.breed = 'siam'
# Изменение значения атрибута breed в экземпляре d, вызвало изменение значения этого атрибута
# в экземплярях f и g (во всех экземплярах класса Cat2)
print(d.breed)
print(f.breed)
print(g.breed)
print()

# Добавление атрибута name в экземпляре d, также вызовет добавление этого атрибута
# в экземплярях f и g (во всех экземплярах класса Cat2)
d.name = 'Bob'
print(d.__dict__)
print(f.__dict__)
print(g.__dict__)
print()

# Новый экземпляр h класса Cat2 вберёт в себя все изменения, произошедшие с уже созданными экземплярами класса Cat2
h = Cat2()
print(h.__dict__)
print()
