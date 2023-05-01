#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(s, t, combo):
    if len(s) + len(t) != len(combo):
        return False

    if len(combo) == 0:
        return True

    if len(s) == 0:
        return solution(s, t[1:], combo[1:])

    if len(t) == 0:
        return solution(s[1:], t, combo[1:])

    if s[0] == t[0]:
        if s[0] != combo[0]:
            return False

        result = solution(s, t[1:], combo[1:])
        if not result:
            result = solution(s[1:], t, combo[1:])

        return result

    if s[0] == combo[0]:
        return solution(s[1:], t, combo[1:])

    return solution(s, t[1:], combo[1:])


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        expecting = True
        self.assertEqual(expecting, solution(s1, s2, s3))

    def test_2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        expecting = False
        self.assertEqual(expecting, solution(s1, s2, s3))

    def test_3(self):
        s1 = ""
        s2 = ""
        s3 = ""
        expecting = True
        self.assertEqual(expecting, solution(s1, s2, s3))

