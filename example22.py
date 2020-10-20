from lesson22 import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_rect_area(), rect2.get_rect_area())
print('---------------------------')

sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_sq_area(), sq2.get_sq_area())
print('---------------------------')

cir1 = Circle(5)
cir2 = Circle(2)
print(cir1.get_circle_area(), cir2.get_circle_area())
print('---------------------------')

figures = [rect1, rect2, sq2, sq1, cir2, cir1]
for figure in figures:
    # Проблема
    # try:
    #     print(figure.get_rect_area())       # у экземпляра Square нет метода get_rect_area()
    #     print(figure.get_sq_area())         # у экземпляра Rectangle нет метода get_sq_area()
    # except AttributeError as ae:
    #     print(ae)

    # Решение 1
    if isinstance(figure, Rectangle):
        print(figure.get_rect_area())

    elif isinstance(figure, Circle):
        print(figure.get_circle_area())

    else:
        print(figure.get_sq_area())
    print('---------------------------')

    # Решение 2 (хочется работать с каждым экземпляром одинаково, но при этом каждый экземпляр вёл себя по разному)
    for figure in figures:
        print(figure, " S=", figure.get_area())    # figure неявно вызовет __str__
print('---------------------------')
