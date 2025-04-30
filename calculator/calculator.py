import math
from decimal import Decimal, getcontext


class ShapeAreaCalculator:

    def area_circle(self, radius):
        """
        Вычисляет площадь круга по радиусу.
        Установим точность для Decimal
        """
        if radius < 0:
            raise ValueError("Радиус не может быть меньше нуля")
        getcontext().prec = 28
        pi = Decimal('3.141592653589793238')
        area = pi * (Decimal(radius) ** 2)
        return area.quantize(Decimal('0.01'))

    def area_triangle(self, a, b, c):
        """Вычисляет площадь треугольника по трём сторонам"""
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть больше нуля")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Стороны не образуют треугольник")

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return Decimal(area).quantize(Decimal('0.01'))

    def is_triangle_right(self, a, b, c):
        """Проверяет, является ли треугольник прямоугольным"""
        right = sorted([a, b, c])
        return right[0] ** 2 + right[1] ** 2 == right[2] ** 2

    def area(self, shape, *args):
        """Вычисляет площадь фигуры без знания типа в compile-time"""
        if shape == 'circle':
            return self.area_circle(*args)
        if shape == 'triangle':
            return self.area_triangle(*args)
        else:
            raise ValueError("Неизвестный тип фигуры")


if __name__ == "__main__":
    calculator = ShapeAreaCalculator()

    circle_area = calculator.area('circle', 10)
    print(f"Площадь круга: {circle_area}")

    triangle_area = calculator.area('triangle', 4, 5, 6)
    print(f"Площадь треугольника: {triangle_area}")

    is_right = calculator.is_triangle_right(3, 4, 5)
    print(f"Треугольник прямоугольный: {is_right}")
