import unittest
from investment.investment import *


class test(unittest.TestCase):
    
    """Unit-testing class that allows us to run tests with expected outcomes"""

    def test_constructor(self):
        
        """
        unit test for the investment costructor that passinput
        to arguments positions and num_trials
        """    
        
        self.assertEqual(investment([1,10,100], 1000).positions,[1,10,100])
        self.assertEqual(investment([1,10,100], 1000).num_trials, 1000)
        
    def test_stimulate(self):
        
        """
        unit tests for function stimulate
            We test the each value of the return dictionary 'result' has the same length as
            num_trials, and every element in the value of dictionary 'result' bigger than 
            or equal to -1, and less than or equal to 1 
        """
        t = investment([1, 10, 100], 1000)
        result = t.stimulate([1000.0, 100.0, 10.0], 1000) 
 
        self.assertEqual(len(result[1]), 1000)
        self.assertEqual(len(result[10]), 1000)
        self.assertEqual(len(result[100]), 1000)
 
        self.assertTrue(result[1].all() <= 1)
        self.assertTrue(result[1].all() >= -1)
 
        self.assertTrue(result[10].all() <= 1)
        self.assertTrue(result[10].all() >= -1)
 
        self.assertTrue(result[100].all() <= 1)
        self.assertTrue(result[100].all() >= -1)    
            
    
if __name__ == "__main__":
    unittest.main()