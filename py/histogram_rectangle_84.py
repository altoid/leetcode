#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(arr):
    # this will force us to process the stack one more time.
    arr.append(0)

    # stack holds indices
    stack = [0]

    max_area = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[stack[-1]]:
            stack.append(i)
            continue

        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            b = stack.pop()
            width = i
            if stack:
                width -= (stack[-1] + 1)
            max_area = max(max_area, arr[b] * width)
        stack.append(i)

    return max_area


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_5(self):
        arr = [0]
        expected = 0
        self.assertEqual(expected, solution(arr))

    def test_4(self):
        arr = [5, 4, 4, 5]
        expected = 16
        self.assertEqual(expected, solution(arr))

    def test_3(self):
        arr = []
        expected = 0
        self.assertEqual(expected, solution(arr))

    def test_2(self):
        arr = [6]
        expected = 6
        self.assertEqual(expected, solution(arr))

    def test_1(self):
        arr = [6, 2, 9, 4, 5, 1, 6]
        expected = 12
        self.assertEqual(expected, solution(arr))
