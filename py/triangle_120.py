#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random

#
# to find next set of indexes
# start from right
# find rightmost pair where values are equal
# output
# increment the right of the pair and set everything to the right of THAT to the same value
# output
# find rightmost pair where diff is 1
# increment the left of the pair
# output
# start over

def helper(arr, row, stack):
    if row == len(arr):
        result = 0
        p = 0
        while p < len(stack):
            result += arr[p][stack[p]]
            p += 1
        yield result
        return

    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        for j in helper(arr, row + 1, stack):
            yield j
        stack.pop()


def paths(arr):
    stack = [0]
    row = 1
    for i in range(stack[row - 1], stack[row - 1] + 2):
        stack.append(i)
        for j in helper(arr, row + 1, stack):
            yield j
        stack.pop()


def solution(arr):
    if len(arr) == 1:
        return arr[0][0]
    return min(paths(arr))


if __name__ == '__main__':
    arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    for x in paths(arr):
        print(x)

    print(min(paths(arr)))


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
