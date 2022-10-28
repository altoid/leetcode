#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(s, p):
    if len(p) > len(s):
        return []

    stop = len(s) - len(p) + 1
    psorted = ''.join(sorted(list(p)))
    result = []

    x = 0
    while x < stop:
        e = sorted(list(enumerate(s[x:x + len(p)])), key=lambda x: x[1])
        i = 0
        while i < len(p):
            if psorted[i] != e[i][1]:
                break
            i += 1

        if i == len(p):
            result.append(x)
            x += 1
            continue

        # if the character that stopped the comparison is in p, increment by 1.  otherwise,
        # increment to the character after it.
        if e[i][1] in p:
            x += 1
        else:
            x = x + e[i][0] + 1

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