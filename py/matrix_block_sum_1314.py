#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random

band_cache = {}


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


def solution(matrix, k):
    pass


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
    def test_1(self):
        matrix = make_matrix(6, 7)
        k = 1
        pprint(matrix)

        self.assertEqual(9, band_sum(matrix, 0, 0, k))
        self.assertEqual(24, band_sum(matrix, 1, 0, k))
        self.assertEqual(45, band_sum(matrix, 2, 0, k))
        self.assertEqual(66, band_sum(matrix, 3, 0, k))
        self.assertEqual(87, band_sum(matrix, 4, 0, k))
        self.assertEqual(65, band_sum(matrix, 5, 0, k))
