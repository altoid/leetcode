#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random

band_cache = None
block_cache = None


def band_sum(matrix, r, c, k):
    nrows = len(matrix)
    global band_cache
    band_from = max(0, r - k)
    band_to = min(nrows, r + k + 1)

    key = (band_from, band_to, c)
    if key not in band_cache:
        if r > 0:
            result = band_sum(matrix, r - 1, c, k)
            previous_band_from = max(0, r - k - 1)
            previous_band_to = min(nrows, r + k)
            if previous_band_from < band_from:
                result = result - matrix[previous_band_from][c]
            if previous_band_to < band_to:
                result = result + matrix[band_to - 1][c]
        else:
            result = sum([matrix[x][c] for x in range(band_from, band_to)])

        band_cache[key] = result

    return band_cache[key]


def block_sum(matrix, r, c, k):
    global block_cache
    global band_cache

    nrows = len(matrix)
    ncolumns = len(matrix[0])

    block_first_row = max(0, r - k)
    block_last_row = min(nrows, r + k + 1)
    block_first_column = max(0, c - k)
    block_last_column = min(ncolumns, c + k + 1)

    key = (block_first_row, block_first_column, block_last_row, block_last_column)

    if key not in block_cache:
        if c > 0:
            result = block_sum(matrix, r, c - 1, k)
            previous_first_column = max(0, c - k - 1)
            previous_last_column = min(ncolumns, c + k)
            if previous_first_column < block_first_column:
                result = result - band_sum(matrix, r, previous_first_column, k)
            if previous_last_column < block_last_column:
                result = result + band_sum(matrix, r, block_last_column - 1, k)
        else:
            result = sum([band_sum(matrix, r, x, k) for x in range(block_first_column, block_last_column)])

        block_cache[key] = result

    return block_cache[key]


def solution(matrix, k):
    result = []
    nrows = len(matrix)
    ncolumns = len(matrix[0])

    for r in range(nrows):
        row = [block_sum(matrix, r, x, k) for x in range(ncolumns)]
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
    def setUp(self):
        global band_cache
        global block_cache
        band_cache = {}
        block_cache = {}

    def test_4(self):
        matrix = make_matrix(3, 3)
        k = 1
        result = solution(matrix, k)
        pprint(result)

    def test_3(self):
        matrix = make_matrix(6, 7)
        k = 1

        self.assertEqual(20, block_sum(matrix, 0, 0, 1))

    def test_2(self):
        matrix = make_matrix(6, 7)
        k = 1
        # pprint(matrix)

        self.assertEqual(9, band_sum(matrix, 0, 0, k))
        self.assertEqual(24, band_sum(matrix, 1, 0, k))
        self.assertEqual(45, band_sum(matrix, 2, 0, k))
        self.assertEqual(66, band_sum(matrix, 3, 0, k))
        self.assertEqual(87, band_sum(matrix, 4, 0, k))
        self.assertEqual(65, band_sum(matrix, 5, 0, k))

    def test_1(self):
        matrix = make_matrix(6, 7)
        k = 9
        # pprint(matrix)

        self.assertEqual(111, band_sum(matrix, 0, 0, k))
        self.assertEqual(111, band_sum(matrix, 1, 0, k))
        self.assertEqual(111, band_sum(matrix, 2, 0, k))
        self.assertEqual(111, band_sum(matrix, 3, 0, k))
        self.assertEqual(111, band_sum(matrix, 4, 0, k))
        self.assertEqual(111, band_sum(matrix, 5, 0, k))
