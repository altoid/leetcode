#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def my_multiply(a, b):
    big = max(abs(a), abs(b))
    small = min(abs(a), abs(b))

    product = 0
    for i in range(small):
        product += big

    if (a < 0) != (b < 0):
        product = -product

    return product


def powers(a, upto):
    result = [1, a]

    while True:
        p = 0
        i = 0
        while i < a:
            i += 1
            p += result[-1]
            if p > upto:
                break

        if i < a or p > upto:
            break

        result.append(p)

    return result[::-1]


def divide(dividend, divisor):
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)
    parity = 1
    if (dividend < 0) != (divisor < 0):
        parity = -1

    quotient = 0
    if abs_dividend < abs_divisor:
        return quotient

    if abs_divisor == 1:
        quotient = abs_dividend
    else:
        pws = powers(abs_divisor, abs_dividend)
        pws = list(enumerate(pws))

        # start from the beginning and find the biggest power >= the dividend
        for x in pws[:-1]:
            if x[1] > abs_dividend:
                continue

            while abs_dividend - x[1] >= 0:
                quotient += pws[x[0] + 1][1]
                abs_dividend -= x[1]

    quotient *= parity

    if quotient > 0:
        quotient = min(quotient, 2 ** 31 - 1)
    elif quotient < 0:
        quotient = max(quotient, -2 ** 31)

    return quotient


if __name__ == '__main__':
    # print(powers(2, 2147483647))

    #dividend = 1000000
    #divisor = 3
    dividend = 1026117192
    divisor = 874002063
    pws = powers(divisor, dividend)
    pws = list(enumerate(pws))
    quotient = 0

    print(pws)

class MyTest(unittest.TestCase):
    def test_6(self):
        dividend = 1026117192
        divisor = 874002063
        expecting = 1
        self.assertEqual(expecting, divide(dividend, divisor))

    def test_1(self):
        expecting = [3 * 3 * 3 * 3, 3 * 3 * 3, 3 * 3, 3, 1]
        result = powers(3, 100)
        self.assertEqual(expecting, result)

    def test_2(self):
        expecting = [3 * 3 * 3 * 3, 3 * 3 * 3, 3 * 3, 3, 1]
        result = powers(3, 3 ** 4)
        self.assertEqual(expecting, result)

    def test_3(self):
        dividend = 7
        divisor = -3
        expecting = -2
        self.assertEqual(expecting, divide(dividend, divisor))

    def test_4(self):
        dividend = 2147483647
        divisor = 2
        expecting = 1073741823
        self.assertEqual(expecting, divide(dividend, divisor))

    def test_5(self):
        dividend = 1004958205
        divisor = -2137325331
        expecting = 0
        self.assertEqual(expecting, divide(dividend, divisor))

