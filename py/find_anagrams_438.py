#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(s, p):
    width = len(p)
    if width > len(s):
        return []

    stop = len(s) - width + 1
    pdict = {}
    for k in p:
        if k not in pdict:
            pdict[k] = 0
        pdict[k] += 1

    result = []

    sdict = {}
    for k in s[:len(p)]:
        if k not in sdict:
            sdict[k] = 0
        sdict[k] += 1

    x = 0
    while x < stop:
        if sdict == pdict:
            result.append(x)

        if x + width >= len(s):
            break
        c = s[x]
        sdict[c] -= 1
        if sdict[c] == 0:
            del sdict[c]

        c = s[x + width]
        if c not in pdict:
            x = x + width + 1
            sdict = {}
            for k in s[x:x+len(p)]:
                if k not in sdict:
                    sdict[k] = 0
                sdict[k] += 1

            continue

        if c not in sdict:
            sdict[c] = 0
        sdict[c] += 1

        x += 1

    return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    r = solution(s, p)
    print(r)


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "cbaebabacd"
        p = "abc"
        r = solution(s, p)
        print(r)
        self.assertEqual([0, 6], sorted(r))

    def test_2(self):
        s = "abab"
        p = "ab"
        r = solution(s, p)
        print(r)
        self.assertEqual([0, 1, 2], sorted(r))

    def test_3(self):
        s = "abcxabc"
        p = "abc"
        r = solution(s, p)
        print(r)
        self.assertEqual([0, 4], sorted(r))

