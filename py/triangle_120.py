#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(arr):
    # can't do it by evaluating paths; that is O(2 ** n)
    # use memoization

    n = len(arr)
    tableau = [[None] * n for _ in range(n)]

    tableau[0][0] = arr[0][0]

    for r in range(1, n):
        for c in range(r + 1):
            predecessors = []
            if c < r:
                predecessors.append(tableau[r - 1][c])
            if c > 0:
                predecessors.append(tableau[r - 1][c - 1])

            v = arr[r][c]
            if predecessors:
                v += min(predecessors)

            tableau[r][c] = v

    return min(tableau[-1])


def solution_2():
    arr = [0] * 44

    # start out with an array of 0s.  increment the values in the array such that
    #
    # 1.  the difference between a value and the value to its right is at most 1.
    # 2.  the rightmost element is never incremented.

    # 0 0 0 0 0
    # 1 0 0 0 0
    # 1 1 0 0 0
    # 2 1 0 0 0
    # 1 1 1 0 0
    #

    # there are 2 ** n paths

    p = 0
    while True:
        while p < len(arr) and arr[p] > arr[p + 1]:
            p += 1
        if p == len(arr) - 1:
            break

        arr[p] += 1
        for i in range(p):
            arr[i] = arr[p]

        print(arr)
        p = 0


if __name__ == '__main__':
    arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(solution(arr))
    # for x in paths(arr):
    #     print(x)
    #
    # print(min(paths(arr)))


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
