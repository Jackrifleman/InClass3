#Jackson Eubank
#CS 362
#InClass 3

import unittest;
import calculator;

class TestCalculator(unittest.TestCase):
    def test_add(self):
        testAdd = calculator.add(4,2);
        self.assertEqual(testAdd,6);
        
    def test_subtract(self):
        testSub = calculator.subtract(12,6);
        self.assertEqual(testSub,6);

    def test_multiply(self):
        testMult = calculator.multiply(5,5);
        self.assertEqual(testMult,25);

    def test_divide(self):
        testDiv = calculator.divide(63,9);
        self.assertEqual(testDiv,7)
        
    def test_divide_by_zero(self):
        self.assertRaises(ValueError,calculator.divide,10,0);


if (__name__ == '__main__'):
    unittest.main();
    
