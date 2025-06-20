import unittest
from knapsack import KnapsackSolver, Item

class TestKnapsackSolver(unittest.TestCase):
    
    def test_knapsack_standard_case(self):
        items_list = (
            Item(value=60, weight=10),
            Item(value=100, weight=20),
            Item(value=120, weight=30),
        )
        self.assertEqual(KnapsackSolver.knapsack(50, items_list, 3), 220)
    
    def test_knapsack_no_items(self):
        items_list = ()
        self.assertEqual(KnapsackSolver.knapsack(50, items_list, 0), 0)
    
    def test_knapsack_zero_capacity(self):
        items_list = (
            Item(value=60, weight=10),
        )
        self.assertEqual(KnapsackSolver.knapsack(0, items_list, 1), 0)
    
    def test_knapsack_item_exceeds_capacity(self):
        items_list = (
            Item(value=100, weight=60),
        )
        self.assertEqual(KnapsackSolver.knapsack(50, items_list, 1), 0)

if __name__ == "__main__":
    unittest.main()