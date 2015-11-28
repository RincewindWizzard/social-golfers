#!/usr/bin/python3
import unittest, random

import sgp

class TestLearning(unittest.TestCase):
  def setUp(self):
    self.solution = sgp.generateSolution(5, 4, 5)#[[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]
    self.tabu = [
      { (1, 2): 2, (1, 3): 2},
      { (1, 2): 2, (1, 3): 1},
    ]

  def test_preffered(self):
    swaps = list(sgp.swaps(self.solution))
    #print(swaps)
    violats = list(map(lambda t: (sgp.evaluate_swap(self.solution, t), t), swaps))
    
    print(min(violats), max(violats))
    """self.assertEqual(
      list(sgp.swaps(self.solution)), 
      None
    )"""

  def test_violations(self):
    self.assertEqual(sgp.violations(self.solution)[0], 6)

if __name__ == '__main__':
    unittest.main()
