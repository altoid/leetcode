#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def width(n):
    c = 0

    while n > 0:
        c += 1
        n = n >> 1

    return c


def solution(left, right):
    # need to identify the high-order bits of the numbers that don't change
    # as you iterate through them.  find left & right.  if there is a leading 0
    # then the answer is 0.  otherwise construct a mask of the form 111...000...
    # and & this with left

    if left == 0:
        return 0

    if right == 0:
        return 0

    # find the width in bits of each.
    if width(right) != width(left):
        return 0

    x = left & right
    if width(x) != width(left):
        return 0

    nextbit = 1
    mask = 0
    p = 1 << (width(x) - 1)
    while p != 0:
        mask <<= 1
        mask |= nextbit
        p >>= 1
        if p & left != p & right:
            nextbit = 0

    return mask & left


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, width(0))
        self.assertEqual(5, width(20))
        self.assertEqual(3, width(7))

    def test_2(self):
        left = 5
        right = 7
        self.assertEqual(4, solution(left, right))

    def test_3(self):
        left = 0
        right = 0
        self.assertEqual(0, solution(left, right))

    def test_4(self):
        left = 0
        right = 2147483647
        self.assertEqual(0, solution(left, right))

