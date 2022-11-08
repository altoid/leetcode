#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(s):
    char_to_count = {}
    first_appearance = {}

    i = 0
    for c in s:
        if c not in char_to_count:
            char_to_count[c] = 0
        char_to_count[c] += 1
        if c not in first_appearance:
            first_appearance[c] = i
        i += 1

    solo_chars = [x[0] for x in filter(lambda x: x[1] == 1, char_to_count.items())][::-1]
    solo_chars = sorted(solo_chars, key=lambda x: first_appearance[x])
    if solo_chars:
        return first_appearance[solo_chars[0]]


if __name__ == '__main__':
    s = "sstringxime"
    print(solution(s))


class MyTest(unittest.TestCase):
    def test_1(self):
        pass
