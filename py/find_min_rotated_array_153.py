#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def helper(arr, a, b):
    if b < a:
        return None

    if a == b:
        return arr[a]

    m = (a + b) // 2

    if arr[a] > arr[m]:
        return helper(arr, a, m)

    if arr[m + 1] > arr[b]:
        return helper(arr, m + 1, b)

    # if a == b, then m == a == b
    # if a + 1 == b, then m = (a + b) // 2 == (a + a + 1) // 2 == (2a + 1) // 2 == a and m + 1 == b

    return min(arr[m + 1], arr[0])


def solution(arr):
    return helper(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        nums = [3, 4, 5, 1, 2]
        expected = 1
        actual = solution(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        actual = solution(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [3]
        expected = 3
        actual = solution(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [1, 2, 3, 4, 5]
        expected = 1
        actual = solution(nums)
        self.assertEqual(expected, actual)

