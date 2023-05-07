#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(arr):
    # we don't actually have to find the LIS.  all we need is the length of the cover.

    cover = []

    for a in arr:
        appended = False
        for c in cover:
            if a <= c[-1]:
                c.append(a)
                appended = True
                break
        if not appended:
            cover.append([a])

    return len(cover)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expecting = 4
        self.assertEqual(expecting, solution(nums))

    def test_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        expecting = 4
        self.assertEqual(expecting, solution(nums))

    def test_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        expecting = 1
        self.assertEqual(expecting, solution(nums))

    def test_4(self):
        nums = []
        expecting = 0
        self.assertEqual(expecting, solution(nums))