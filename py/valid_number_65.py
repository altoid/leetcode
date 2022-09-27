#!/usr/bin/env python

# https://leetcode.com/problems/valid-number/

import unittest
from pprint import pprint
import random
import re


def solution(n):
    pattern = r'^[-+]{0,1}(\d+(\.\d*)?|\.[\d]+)([eE][+-]?\d+)?$'
    result = re.match(pattern, n)
    #    print(n, result)
    return bool(result)


if __name__ == '__main__':
    these_are_valid = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
                       "-123.456e789"]
    for n in these_are_valid:
        print(n, solution(n))

    these_are_invalid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for n in these_are_invalid:
        print(n, solution(n))


class MyTest(unittest.TestCase):
    def test_1(self):
        these_are_valid = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
                           "-123.456e789"]
        for n in these_are_valid:
            self.assertTrue(solution(n))

    def test_2(self):
        these_are_not_valid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
        for n in these_are_not_valid:
            self.assertFalse(solution(n))
