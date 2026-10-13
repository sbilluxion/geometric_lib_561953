from math import pi


def area(r):
#Возвращает площадь круга в формате float
#	Параметры:
#		r: радиус окружности
#	Пример: area(10) = 314.1592653589793	
    if r >= 0:
        return pi * r * r
    else:
        raise ValueError('Радиус должен быть неотрицательным')


def perimeter(r):
#Возвращает периметр круга в формате float
#	Параметры:
#		r: радиус окружности
#	Пример: perimeter(10) = 62.83185307179586
#
    if r >= 0:
        return 2 * pi * r
    else:
        raise ValueError('Радиус должен быть неотрицательным')

