#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(n):
    if n == 0:
        return "0"
    
    result = []
    while n != 0:
        if n & 1:
            result.append('1')
        else:
            result.append('0')
        n = -1 * (n >> 1)

    return ''.join(result[::-1])


def convert_from_bin(s):
    result = 0

    for bit in s:
        result *= -2
        if bit == '1':
            result += 1
    return result


if __name__ == '__main__':
    for _ in range(100000):
        n = random.randint(0, 10 ** 9)
        bv = solution(n)
        verif = convert_from_bin(bv)
        if verif != n:
            print("n = %s, verif = %s" % (n, verif))


class MyTest(unittest.TestCase):
    def test_1(self):
        pass
