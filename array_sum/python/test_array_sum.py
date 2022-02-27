import random
import unittest
from array_sum import ArraySum


class UnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        elements = 1000
        cls.arr_positive = random.sample(range(elements), elements)
        cls.arr_negative = random.sample(range(-elements, 0), elements)

    def test_six_elements(self):
        arr = self.arr_positive[:6]
        actual = ArraySum(arr).array_sum
        expected = sum(arr)
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum({arr}).array_sum'
        )

    def test_one_element(self):
        arr = self.arr_positive[:1]
        actual = ArraySum(arr).array_sum
        expected = sum(arr)
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum({arr}).array_sum'
        )

    def test_empty_array(self):
        arr = []
        actual = ArraySum(arr).array_sum
        expected = 0
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum({arr}).array_sum'
        )

    def test_large_array(self):
        arr = self.arr_positive[5:875]
        actual = ArraySum(arr).array_sum
        expected = sum(arr)
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum(large_array).array_sum'
        )

    def test_array_with_zero(self):
        arr = [0, 0, 0]
        actual = ArraySum(arr).array_sum
        expected = 0
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum({arr}).array_sum'
        )

    def test_negative_elements(self):
        arr = self.arr_negative[:10]
        actual = ArraySum(arr).array_sum
        expected = sum(arr)
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum({arr}).array_sum'
        )

    def test_large_array_negative_elements(self):
        arr = self.arr_negative[1:952]
        actual = ArraySum(arr).array_sum
        expected = sum(arr)
        self.assertEqual(
            actual,
            expected,
            f'Expected {expected} but got {actual} when ArraySum(large_array).array_sum'
        )


if __name__ == '__main__':
    unittest.main()
