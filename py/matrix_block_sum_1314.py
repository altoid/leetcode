#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


class Solution:
    def __init__(self):
        self.band_cache = {}
        self.block_cache = {}

    def band_sum(self, matrix, r, c, k):
        nrows = len(matrix)
        band_from = max(0, r - k)
        band_to = min(nrows, r + k + 1)

        key = (band_from, band_to, c)
        if key not in self.band_cache:
            if r > 0:
                result = self.band_sum(matrix, r - 1, c, k)
                previous_band_from = max(0, r - k - 1)
                previous_band_to = min(nrows, r + k)
                if previous_band_from < band_from:
                    result = result - matrix[previous_band_from][c]
                if previous_band_to < band_to:
                    result = result + matrix[band_to - 1][c]
            else:
                result = sum([matrix[x][c] for x in range(band_from, band_to)])

            self.band_cache[key] = result

        return self.band_cache[key]

    def block_sum(self, matrix, r, c, k):
        nrows = len(matrix)
        ncolumns = len(matrix[0])

        block_first_row = max(0, r - k)
        block_last_row = min(nrows, r + k + 1)
        block_first_column = max(0, c - k)
        block_last_column = min(ncolumns, c + k + 1)

        key = (block_first_row, block_first_column, block_last_row, block_last_column)

        if key not in self.block_cache:
            if c > 0:
                result = self.block_sum(matrix, r, c - 1, k)
                previous_first_column = max(0, c - k - 1)
                previous_last_column = min(ncolumns, c + k)
                if previous_first_column < block_first_column:
                    result = result - self.band_sum(matrix, r, previous_first_column, k)
                if previous_last_column < block_last_column:
                    result = result + self.band_sum(matrix, r, block_last_column - 1, k)
            else:
                result = sum([self.band_sum(matrix, r, x, k) for x in range(block_first_column, block_last_column)])

            self.block_cache[key] = result

        return self.block_cache[key]

    def matrixBlockSum(self, matrix, k):
        result = []
        nrows = len(matrix)
        ncolumns = len(matrix[0])

        for r in range(nrows):
            row = [self.block_sum(matrix, r, x, k) for x in range(ncolumns)]
            result.append(row)
        return result


def make_matrix(nrows, ncolumns):
    result = []
    for r in range(nrows):
        row = [x for x in range(r * ncolumns + 1, r * ncolumns + ncolumns + 1)]
        result.append(row)

    return result


if __name__ == '__main__':
    matrix = make_matrix(6, 7)
    pprint(matrix)


class MyTest(unittest.TestCase):
    def test_4(self):
        matrix = make_matrix(3, 3)
        k = 1
        solution = Solution()
        result = solution.matrixBlockSum(matrix, k)
        pprint(result)

    def test_3(self):
        matrix = make_matrix(6, 7)
        k = 1
        solution = Solution()

        self.assertEqual(20, solution.block_sum(matrix, 0, 0, 1))

    def test_2(self):
        matrix = make_matrix(6, 7)
        k = 1
        solution = Solution()
        # pprint(matrix)

        self.assertEqual(9, solution.band_sum(matrix, 0, 0, k))
        self.assertEqual(24, solution.band_sum(matrix, 1, 0, k))
        self.assertEqual(45, solution.band_sum(matrix, 2, 0, k))
        self.assertEqual(66, solution.band_sum(matrix, 3, 0, k))
        self.assertEqual(87, solution.band_sum(matrix, 4, 0, k))
        self.assertEqual(65, solution.band_sum(matrix, 5, 0, k))

    def test_1(self):
        matrix = make_matrix(6, 7)
        k = 9
        solution = Solution()
        # pprint(matrix)

        self.assertEqual(111, solution.band_sum(matrix, 0, 0, k))
        self.assertEqual(111, solution.band_sum(matrix, 1, 0, k))
        self.assertEqual(111, solution.band_sum(matrix, 2, 0, k))
        self.assertEqual(111, solution.band_sum(matrix, 3, 0, k))
        self.assertEqual(111, solution.band_sum(matrix, 4, 0, k))
        self.assertEqual(111, solution.band_sum(matrix, 5, 0, k))
