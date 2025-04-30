import unittest
from calculator import ShapeAreaCalculator


class TestShapeAreaCalculator(unittest.TestCase):
    
    def setUp(self):
        """Настройка для тестового класса.
        Создает экземпляр ShapeAreaCalculator."""
        self.calculator = ShapeAreaCalculator()

    def test_area_circle(self):
        """Тестирует метод area для расчета площади круга."""
        self.assertAlmostEqual(self.calculator.area('circle', 5), 78.53981633974483)
        with self.assertRaises(ValueError):
            self.calculator.area('circle', -1)

    def test_area_triangle(self):
        """Тестирует метод area для расчета площади треугольника."""
        self.assertAlmostEqual(self.calculator.area('triangle', 3, 4, 5), 6.0)
        with self.assertRaises(ValueError):
            self.calculator.area('triangle', 1, 1, 3)

    def test_is_triangle_right(self):
        """Тестирует метод is_triangle_right для проверки прямоугольности треугольника."""
        self.assertTrue(self.calculator.is_triangle_right(3, 4, 5))
        self.assertFalse(self.calculator.is_triangle_right(2, 2, 3))

    def test_area_unknown_shape(self):

        """Тестирует метод area на обработку неизвестного типа фигуры."""
        with self.assertRaises(ValueError):
            self.calculator.area('unknown_shape', 1, 1, 1)


if __name__ == '__main__':
    unittest.main()
