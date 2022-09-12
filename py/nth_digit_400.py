#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(n: int):
    offset = n - 1
    i = 0
    # subtrahend is equal to the number of digits in all (i + 1) digit numbers
    # (excluding leading 0s)

    subtrahend = 10 ** i * 9 * (i + 1)
    while offset > subtrahend:
        offset -= subtrahend
        i += 1
        subtrahend = 10 ** i * 9 * (i + 1)

    # i is the power of 10 block that contains the digit

    ndigits = i + 1

    q, r = divmod(offset, ndigits)
    block = 10 ** (ndigits - 1)
    number = block + q
    digit = int(str(number)[r])
    return digit


if __name__ == '__main__':
    l = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]
    for n in l:
        print("%s, %s" % (n, solution(n)))


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, solution(1))

    def test1_2(self):
        self.assertEqual(1, solution(10))

    def test1_5(self):
        self.assertEqual(0, solution(11))

    def test2(self):
        self.assertEqual(7, solution(10000))
        self.assertEqual(2, solution(100000))

    def test3(self):
        self.assertEqual(9, solution(148852))
        self.assertEqual(9, solution(148853))
        self.assertEqual(2, solution(148854))
        self.assertEqual(3, solution(148855))
        self.assertEqual(1, solution(148856))
        self.assertEqual(9, solution(148857))

    def test5(self):
        self.assertEqual(3, solution(97))
        self.assertEqual(4, solution(99))

    def test6(self):
        self.assertEqual(5, solution(100))

    def test7(self):
        self.assertEqual(3, solution(1000))
