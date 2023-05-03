#!/usr/bin/env python

# url for problem here

# answer can be monotone nondecreasing

# idea:  use a sliding partition.
#
# input:  1001100
#
#       1   0   0   1   1   0   0
#   0 |                              4    4
#   1     |                          4    5
#   1         |                      3    4
#   1             |                  2    3  *
#   2                 |              2    4   
#   3                     |          2    5   
#   3                         |      1    4   
#   3                             |  0    3  *

import unittest
from pprint import pprint
import random


def solution(s):
    zeroes_count = 0
    for c in s:
        if c == '0':
            zeroes_count += 1

    ones_to_flip = 0
    min_flips = zeroes_count
    for c in s:
        if c == '1':
            ones_to_flip += 1
        else:
            zeroes_count -= 1
        min_flips = min(min_flips, ones_to_flip + zeroes_count)

    return min_flips


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        s = '00110'
        expecting = 1
        self.assertEqual(expecting, solution(s))

    def test_2(self):
        s = '010110'
        expecting = 2
        self.assertEqual(expecting, solution(s))

    def test_3(self):
        s = '00011000'
        expecting = 2
        self.assertEqual(expecting, solution(s))

    def test_4(self):
        s = '111110'
        expecting = 1
        self.assertEqual(expecting, solution(s))

    def test_5(self):
        s = '00000'
        expecting = 0
        self.assertEqual(expecting, solution(s))

    def test_6(self):
        s = '11111'
        expecting = 0
        self.assertEqual(expecting, solution(s))

