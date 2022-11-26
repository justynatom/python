import unittest

from fields import square_area, triangle_area, rectangle_area, trapezoid_area

class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        print("ustawiam warotsci")
        self.a = 50
        self.b = 60
        self.h = 10

    def test_square_area_with_correct_value(self):
        result_s = square_area(self.a)
        self.assertEqual(result_s, 2500)

    def test_square_area_with_incorrect_values(self):
        #self.assertRaises(ValueError, square_area, "$")
        with self.assertRaises(ValueError):
            square_area("$")

    def test_triangle_area_with_correct_value(self):
        result_t = triangle_area(self.a, self.b)
        self.assertEqual(result_t, 1500)

    def test_triangle_area_with_incorrect_values(self):
        #self.assertRaises(ValueError, square_area, "$")
        with self.assertRaises(ValueError):
            triangle_area(self.a, "B")

    def test_rectangle_area_with_correct_value(self):
        result_r = rectangle_area(self.a, self.b)
        self.assertEqual(result_r, 3000)

    def test_rectangle_area_with_incorrect_values(self):
        #self.assertRaises(ValueError, square_area, "$")
        with self.assertRaises(ValueError):
            rectangle_area(self.a, "B")

    def test_trapezoid_area_with_correct_value(self):
        result = trapezoid_area(self.a, self.b, self.h)
        self.assertEqual(result, 550)

    def test_trapezoid_area_with_incorrect_values(self):
        #self.assertRaises(ValueError, square_area, "$")
        with self.assertRaises(ValueError):
            trapezoid_area(self.a, "H", self.b)


    def tearDown(self):
        del self.a
        del self.b
        print("usunieto atrybuty")


if __name__ == '__main__':
    unittest.main()
