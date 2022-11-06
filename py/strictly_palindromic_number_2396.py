#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def convert_to_base(n, base):
    """
    returns an array of decimal numbers indicating multiples of powers of bases
    """
    digits = []
    while n > 0:
        d = n % base
        digits.append(d)
        n = n // base

    return digits[::-1]


def solution(n):
    for b in range(2, n - 1):
        digits = convert_to_base(n, b)
        if digits != digits[::-1]:
            return False
    return True


if __name__ == '__main__':
    print(convert_to_base(9, 2))


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertFalse(solution(9))
