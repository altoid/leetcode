#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def helper(arr, row, stack):
    if row == len(arr):
        result = []
        i = 0
        while i < len(stack):
            result.append(arr[i][stack[i]])
            i += 1
        print(stack, result)
        return

    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        helper(arr, row + 1, stack)
        stack.pop()


def solution(arr):
    stack = [0]
    row = 1
    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        helper(arr, row + 1, stack)
        stack.pop()


if __name__ == '__main__':
    arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    solution(arr)


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        self.assertEqual(11, solution(arr))

