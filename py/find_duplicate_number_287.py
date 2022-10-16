#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def find_cycle_start(arr, start):
    # pretend arr is 1-based
    #
    # use floyd's cycle start detection algorithm:
    # https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
    #
    # for this problem we know we will encounter a cycle, so don't check for running off the end.
    # we just have to figure out whether the cycle begins at the start node or not.
    #
    # return the node that is at the beginning of the cycle.  the caller can determine whether
    # it is the same as the start none.

    slow = start
    fast = start
    while True:
        slow = arr[slow - 1]
        fast = arr[fast - 1]
        fast = arr[fast - 1]
        # print(slow, fast)
        if fast == slow:
            break

    if fast == start:
        # cycle begins at start node.  no node in the cycle has indegree > 1.
        return start

    slow = start
    while True:
        slow = arr[slow - 1]
        fast = arr[fast - 1]
        # print(slow, fast)
        if fast == slow:
            break

    return fast


def solution(arr):
    for a in range(len(arr)):
        b = a + 1
        start = find_cycle_start(arr, b)
        #print("start:  %s, cycle begins:  %s" % (a + 1, start))
        if b != start:
            return start


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 2]
    solution(arr)


class SolutionTest(unittest.TestCase):
    def test_2(self):
        arr = [3, 1, 3, 4, 2]
        self.assertEqual(3, solution(arr))

    def test_1(self):
        arr = [1, 3, 4, 2, 2]
        self.assertEqual(2, solution(arr))


class CycleTest(unittest.TestCase):
    def test_5(self):
        arr = [3, 1, 3, 4, 2]
        self.assertEqual(3, find_cycle_start(arr, 1))
        self.assertEqual(3, find_cycle_start(arr, 2))
        self.assertEqual(3, find_cycle_start(arr, 5))
        self.assertEqual(4, find_cycle_start(arr, 4))

    def test_4(self):
        arr = [1, 3, 4, 2, 2]
        self.assertEqual(2, find_cycle_start(arr, 5))

    def test_3(self):
        arr = [1]
        self.assertEqual(1, find_cycle_start(arr, 1))

    def test_2(self):
        # there's a cycle but also a leading trail
        arr = [2, 3, 4, 5, 6, 7, 8, 9, 4]
        self.assertEqual(4, find_cycle_start(arr, 2))

    def test_1(self):
        # there's a cycle but no leading trail
        arr = [2, 3, 4, 5, 1]
        self.assertEqual(1, find_cycle_start(arr, 1))
