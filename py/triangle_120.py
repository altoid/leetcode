#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def helper(arr, row, stack):
    if row == len(arr):
        print("1. ", [stack[-1]])
        yield [stack[-1]]
        return

    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        for r in helper(arr, row + 1, stack):
            print("2. ", [stack[-1]] + r)
            yield [stack[-1]] + r
        stack.pop()


def sums(arr):
    stack = [0]
    row = 1
    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        for _ in helper(arr, row + 1, stack):
            print("3. ", stack)
            yield stack
        stack.pop()


def solution(arr):
    result = min(list(sums(arr)))
    return result


if __name__ == '__main__':
    arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3], [11, 22, 33, 44, 55]]
    for x in sums(arr):
        print(x)


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        self.assertEqual(11, solution(arr))
