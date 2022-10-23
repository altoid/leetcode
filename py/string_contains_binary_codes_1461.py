#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def to_number(s):
    arr = list(map(int, list(s)))
    result = 0
    for b in arr:
        result *= 2
        result += b
    return result


def solution(s, k):
    # if the number of substrings of size k is less than 2 ** k, game over

    l = len(s)
    if l < k:
        return False

    nsubstrings = l - k + 1
    if nsubstrings < 2 ** k:
        return False

    # turn all of the substrings into numbers.  efficiently
    mask = 2 ** k - 1
    n = to_number(s[:k])

    all_values = set()
    all_values.add(n)

    for end in range(k, l):
        n = n * 2
        n &= mask
        if s[end] == '1':
            n += 1
        all_values.add(n)

    for i in range(2 ** k):
        if i not in all_values:
            return False

    return True


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "00110"
        k = 2
        self.assertTrue(solution(s, k))
