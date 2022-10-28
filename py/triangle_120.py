#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def helper(arr, row, stack):
    if row == len(arr):
        yield
        return

    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        for _ in helper(arr, row + 1, stack):
            yield
        stack.pop()


def paths(arr):
    stack = [0]
    row = 1
    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        for _ in helper(arr, row + 1, stack):
            result = []
            p = 0
            while p < len(stack):
                result.append(arr[p][stack[p]])
                p += 1
            yield result
        stack.pop()


def solution(arr):
    if len(arr) == 1:
        return arr[0][0]
    return min(map(sum, paths(arr)))


if __name__ == '__main__':
    arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3], [11, 22, 33, 44, 55]]
    for x in paths(arr):
        print(x)

    print(min(map(sum, paths(arr))))


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        self.assertEqual(11, solution(arr))

    def test_2(self):
        arr = [[-10]]
        self.assertEqual(-10, solution(arr))

    def test_3(self):
        arr = [[-10], [1, -1]]
        self.assertEqual(-11, solution(arr))
