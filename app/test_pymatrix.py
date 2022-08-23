"""
Testing pymatrix functions
"""
import unittest
from app import pymatrix


class TestPyMatrix(unittest.TestCase):
    """Some test cases for pymatrix function"""
    def setUp(self):
        """Prepare testing data"""
        self.A = [[2, 1, -1], [0, 2, 3]]
        self.B = [[3, 2, 0], [-10, -4, 4]]

    def test_size_of(self):
        """Testing the size of given matrix"""
        self.assertEqual(pymatrix.size_of(matrix=self.A), (2, 3))

    def test_sum_of(self):
        """Testing the sum of two given matrix"""
        self.assertEqual(pymatrix.sum_of(A=self.A, B=self.B),
                         [[5, 3, -1], [-10, -2, 7]])

    def test_sum_of_with_different_size(self):
        """Testing the different size expection of sum_of function"""
        B = [[3, 2, 0], [-10, -4, 4], [1, 2, 3]]

        with self.assertRaisesRegex(ValueError, 'Must have the same size') as _:
            print(pymatrix.sum_of(A=self.A, B=B), [[5, 3, -1], [-10, -2, 7]])
