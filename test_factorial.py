'''
Letisia Tatimoa Pangata'a
COMPSCI 280 - Lab 05 
Student ID : 995182480
'''

import unittest # Import the unittest framework.
import factorial # Import Logger code.


class FactorialTest(unittest.TestCase): # Create a Factorial unittest class.

    def test_factorial(self): # Refer to factorial method.
        
        #1. Arrange / #2. Actual (Sample Integers)
        num1 = 2
        num2 = 1
        
        
        #3. Assert (If the number can be divided (modulo) then it will equal 0)
        self.assertEqual(factorial.factorial(num1, num2), 0) 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()