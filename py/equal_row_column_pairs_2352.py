#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(grid):
    # construct dicts for tuples of the rows and columns.  each tuple will map to the count.
    row_dict = {}
    for r in grid:
        t = tuple(r)
        if t not in row_dict:
            row_dict[t] = 0
        row_dict[t] += 1

    column_dict = {}
    for i in range(len(grid[0])):
        column = tuple(x[i] for x in grid)
        if column not in column_dict:
            column_dict[column] = 0
        column_dict[column] += 1

    total = 0
    for c in column_dict.keys():
        if c in row_dict:
            total += column_dict[c] * row_dict[c]

    return total


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        expecting = 3
        self.assertEqual(expecting, solution(grid))

    def test_2(self):
        grid = [[1]]
        expecting = 1
        self.assertEqual(expecting, solution(grid))
