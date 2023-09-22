import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_base_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base(10)
        self.assertEqual(base3.id, 10)

    def test_base_to_json_string(self):
        base = Base()
        self.assertEqual(base.to_json_string(None), "[]")
        self.assertEqual(base.to_json_string([]), "[]")
        self.assertEqual(base.to_json_string([{'id': 1}]), '[{"id": 1}]')

class TestRectangle(unittest.TestCase):

    def test_rectangle_init(self):
        rectangle = Rectangle(3, 4, 5, 6)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_rectangle_str(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (3) 0/0 - 3/4")

class TestSquare(unittest.TestCase):

    def test_square_init(self):
        square = Square(2, 3, 4)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_square_area(self):
        square = Square(2)
        self.assertEqual(square.area(), 4)

    def test_square_str(self):
        square = Square(2)
        self.assertEqual(str(square), "[Square] (4) 0/0 - 2")

if __name__ == "__main__":
    unittest.main()
