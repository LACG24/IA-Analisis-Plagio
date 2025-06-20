python
import unittest
from bucket_sort import bucket_sort

class TestBucketSort(unittest.TestCase):
    def test_bucket_sort_ascending(self):
        input_data = [
            {"name": "Alice", "score": 88.5},
            {"name": "Bob", "score": 75.0},
            {"name": "Charlie", "score": 93.2},
            {"name": "David", "score": 85.3},
            {"name": "Eve", "score": 77.8}
        ]
        expected_output = [
            {"name": "Bob", "score": 75.0},
            {"name": "Eve", "score": 77.8},
            {"name": "David", "score": 85.3},
            {"name": "Alice", "score": 88.5},
            {"name": "Charlie", "score": 93.2}
        ]
        result = bucket_sort(input_data, key="score")
        self.assertEqual(result, expected_output)
        
    def test_bucket_sort_empty(self):
        input_data = []
        expected_output = []
        result = bucket_sort(input_data, key="score")
        self.assertEqual(result, expected_output)

    def test_bucket_sort_invalid_key(self):
        input_data = [{"name": "Alice", "score": 88.5}]
        with self.assertRaises(KeyError):
            bucket_sort(input_data, key="grade")

    def test_bucket_sort_non_numeric_key(self):
        input_data = [{"name": "Alice", "score": "eighty"}]
        with self.assertRaises(ValueError):
            bucket_sort(input_data, key="score")

if __name__ == "__main__":
    unittest.main()