#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(s1, s2):
    # identify the longest common prefix of each string.  then look ahead 1 char in each.
    # the biggest of these prefixes is appended to the result.
    #
    # 'a' precedes 'aa'.

    result = ""
    p1a = 0
    p2a = 0

    while p1a < len(s1) and p2a < len(s2):
        p1 = p1a
        p2 = p2a

        while p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1

        if p1 < len(s1) and p2 < len(s2):
            # if we come to a char that stops the traversal, keep moving the pointer on the "bigger" string as
            # long as the char we are pointing to is bigger than the one in the other string.
            if s1[p1] > s2[p2]:
                while p1 < len(s1) and s1[p1] > s2[p2]:
                    p1 += 1
                result += s1[p1a:p1]
                p1a = p1
            elif s1[p1] < s2[p2]:
                while p2 < len(s2) and s1[p1] < s2[p2]:
                    p2 += 1
                result += s2[p2a:p2]
                p2a = p2
        elif p1 < len(s1):
            result += s1[p1a:p1 + 1]
            p1a = p1 + 1
        else:
            result += s2[p2a:p2 + 1]
            p2a = p2 + 1

    if p1a < len(s1):
        result += s1[p1a:]
    elif p2a < len(s2):
        result += s2[p2a:]

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_0(self):
        s1 = ""
        s2 = ""
        expecting = ""
        self.assertEqual(expecting, solution(s1, s2))

    def test_1(self):
        s1 = "cabaa"
        s2 = "bcaaa"
        expecting = "cbcabaaaaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_2(self):
        s1 = "abcabc"
        s2 = "abdcaba"
        expecting = "abdcabcabcaba"
        self.assertEqual(expecting, solution(s1, s2))

    def test_3(self):
        s1 = "cabaa"
        s2 = ""
        expecting = "cabaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_4(self):
        s1 = ""
        s2 = "cabaa"
        expecting = "cabaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_5(self):
        s1 = "cabaa"
        s2 = "z"
        expecting = "zcabaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_6(self):
        s1 = "uuurr"
        s2 = "urrr"
        expecting = "uuuurrrrr"
        self.assertEqual(expecting, solution(s1, s2))

    def test_7(self):
        s1 = "uuurruuuruuuuuuuuruuuuu"
        s2 = "urrrurrrrrrrruurrrurrrurrrrruu"
        expecting = "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"
        self.assertEqual(expecting, solution(s1, s2))

