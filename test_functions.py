import unittest
from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c

class TestFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add("space", "ship"), "spaceship")
        
    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(3, 3), 9)
        
    def test_convert_fahrenheit_to_celsius(self):
        self.assertEqual(f2c(32), 0.0)
        self.assertAlmostEqual(f2c(122), 50.0, places=5)
        with self.assertRaises(AssertionError):
            f2c(-600)
            
if __name__ == "__main__":
    unittest.main()


# def test_add():
#     assert add(2, 3) == 5
#     assert add('space', 'ship') == 'spaceship'

# # uncomment the following test in step 5
# def test_subtract():
#     assert subtract(2, 3) == -1
    
# def test_multiply():
#     assert multiply(2, 3) == 6
#     assert multiply(3, 3) == 9

# # uncomment the following test in step 11
# def test_convert_fahrenheit_to_celsius():
#     assert f2c(32) == 0
#     assert f2c(122) == pytest.approx(50)
#     with pytest.raises(AssertionError):
#         f2c(-600)
