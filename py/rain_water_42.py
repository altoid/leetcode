#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(arr):
    if not arr:
        return 0

    maxima_from_left = [arr[0]] * len(arr)
    leftmax = maxima_from_left[0]
    for i in range(len(arr)):
        leftmax = max(leftmax, arr[i])
        maxima_from_left[i] = leftmax

    maxima_from_right = [arr[-1]] * len(arr)
    rightmax = maxima_from_right[-1]
    for i in range(-1, -(len(arr) + 1), -1):
        rightmax = max(rightmax, arr[i])
        maxima_from_right[i] = rightmax

    #pprint(maxima_from_left)
    #pprint(maxima_from_right)

    total = 0
    for i in range(len(arr)):
       total += min(maxima_from_left[i], maxima_from_right[i]) - arr[i]

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
