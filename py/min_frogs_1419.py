#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(s):
    d = {}
    for c in 'croak':
        d[c] = 0

    for c in s:
        if c == 'c':
            d[c] += 1
            if d['k'] > 0:
                d['k'] -= 1
        elif c == 'r':
            if d['c'] == 0:
                return -1
            d['c'] -= 1
            d[c] += 1
        elif c == 'o':
            if d['r'] == 0:
                return -1
            d['r'] -= 1
            d[c] += 1
        elif c == 'a':
            if d['o'] == 0:
                return -1
            d['o'] -= 1
            d[c] += 1
        elif c == 'k':
            if d['a'] == 0:
                return -1
            d['a'] -= 1
            d[c] += 1
        else:
            return -1

    for c in 'croa':
        if d[c] != 0:
            return -1

    return d['k']


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, solution('croak'))
        self.assertEqual(-1, solution('creak'))
        self.assertEqual(1, solution('croakcroak'))
        self.assertEqual(2, solution('croacroakk'))
        self.assertEqual(-1, solution('c'))
        self.assertEqual(-1, solution('bullshit'))

