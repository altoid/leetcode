#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(arr, k):
    if not arr or not k:
        return 0

    # count the number of odd numbers
    odds = list(filter(lambda x: x % 2 == 1, arr))
    if len(odds) == 0:
        return 0

    # calculate the distance between each of the odd numbers, or between the end of the array.
    # first get the indices of each of the odd numbers.
    odd_number_indices = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odd_number_indices.append(i)

    degrees_of_freedom = []
    for i in range(len(odd_number_indices) - 1):
        d = odd_number_indices[i + 1] - odd_number_indices[i]
        degrees_of_freedom.append(d)

    d = len(arr) - odd_number_indices[-1]
    degrees_of_freedom.append(d)

    d = odd_number_indices[0] + 1
    degrees_of_freedom = [d] + degrees_of_freedom

    # finally, turn degrees_of_freedom into pairs of adjacent numbers.  pairs[i] gives the degrees of freedom
    # on each side of odd number at i.

    pairs = []
    for i in range(len(degrees_of_freedom) - 1):
        p = degrees_of_freedom[i], degrees_of_freedom[i + 1]
        pairs.append(p)

    result = 0
    for i in range(len(pairs) - k + 1):
        result += pairs[i][0] * pairs[i + k - 1][1]

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_4(self):
        arr = [3, 2, 6, 4, 3, 4, 8, 9, 8, 3, 7, 0, 1, 9, 0]
        k = 3
        expected = 16
        self.assertEqual(expected, solution(arr, k))

    def test_3(self):
        arr = [2, 4, 6]
        k = 1
        expected = 0
        self.assertEqual(expected, solution(arr, k))

    def test_2(self):
        arr = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        k = 2
        expected = 16
        self.assertEqual(expected, solution(arr, k))

    def test_1(self):
        arr = [1, 1, 2, 1, 1]
        k = 3
        expected = 2
        self.assertEqual(expected, solution(arr, k))
