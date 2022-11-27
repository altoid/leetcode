#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


# idea
# starting at level 0, traverse the array looking for 0s that are between larger values.
# change all the 0s that are between those larger values to 1.  count the number of blocks we change.

# keep increasing levels.


def fill_level(arr, level):
    result = 0

    # find the indices of the leftmost and rightmost values that are at least <level>.

    # count the number of values in that interval that are at most <level>.

    i = 0
    while i < len(arr) and arr[i] <= level:
        i += 1
    if i == len(arr):
        return 0

    j = len(arr) - 1
    while j >= 0 and arr[j] <= level:
        j -= 1
    if j < 0:
        return 0

    j += 1
    for x in range(i, j):
        if arr[x] <= level:
            result += 1

    return result


def solution(arr):
    if not arr:
        return 0

    total = 0
    minlevel = min(arr)
    maxlevel = max(arr)

    for l in range(minlevel, maxlevel):
        result = fill_level(arr, l)
        total += result

    return total


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_3(self):
        arr = [0, 7, 1, 4, 6]
        expecting = 7
        self.assertEqual(expecting, solution(arr))

    def test_2(self):
        arr = [4, 2, 0, 3, 2, 5]
        expecting = 9
        self.assertEqual(expecting, solution(arr))

    def test_1(self):
        arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expecting = 6
        self.assertEqual(expecting, solution(arr))
