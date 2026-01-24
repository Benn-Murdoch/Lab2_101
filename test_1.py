import unittest
from lab2_1 import get_first_alphabetically, calculate_triangle_area

class TestLab2(unittest.TestCase):

    # --- Tests for get_first_alphabetically ---
    def test_get_first_1(self):
        self.assertEqual(get_first_alphabetically("a","b"),"a")


    def test_get_first_2(self):
        self.assertEqual(get_first_alphabetically("b","a"),"a")
        


    def test_get_first_3(self):
        self.assertEqual(get_first_alphabetically("A","Z"),"A")
   
   
    # --- Tests for calculate_triangle_area ---
    def test_area_1(self):
        self.assertEqual(calculate_triangle_area(2,3),3.0)


    def test_area_2(self):
        self.assertEqual(calculate_triangle_area(2,9),9.0)


    def test_area_3(self):
        self.assertEqual(calculate_triangle_area(8,8),32.0)


if __name__ == '__main__':
    unittest.main()