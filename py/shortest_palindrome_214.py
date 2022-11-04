#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random
from functools import reduce


def enc_helper(acc, value):
    if acc[-1][0] == value:
        acc[-1][1] += 1
    else:
        acc.append([value, 1])

    return acc


def encode(s):
    if not s:
        return []

    acc = [[s[0], 1]]
    result = reduce(enc_helper, s[1:], acc)

    return result


def decode(enc):
    return ''.join(list(map(lambda x: x[0] * x[1], enc)))


def solution(s):
    # encodings are lists of [char, count]
    s_enc = encode(s)
    s_rev_enc = encode(s[::-1])

    # s = 'aacecaaa'
    # s_enc     = (a 2)(c 1)(e 1)(c 1)(a 3)
    # s_enc_rev = (a 3)(c 1)(e 1)(c 1)(a 2)

    # line them up by char.  new chars have to be added to the front of s

    s_unique_chars = ''.join([x[0] for x in s_enc])
    s_rev_unique_chars = s_unique_chars[::-1]

    for i in range(len(s_rev_unique_chars)):
        l = len(s_rev_unique_chars) - i
        if s_rev_unique_chars[i:] == s_unique_chars[:l]:
            #print("-------")
            #print(s_rev_unique_chars)
            #print("%s%s" % (' ' * i, s_unique_chars))

            k = 0
            if s_rev_enc[i][1] < s_enc[0][1]:
                print("nope for i = %s" % i)
                continue

            # l - i is the number of chars that match
            nmatches = l - i
            k = 1
            equal_overlaps = True
            while k < nmatches - 1:
                if s_rev_enc[i + k][1] != s_enc[k][1]:
                    equal_overlaps = False
                    break
                k += 1
            if not equal_overlaps:
                print("nope for i = %s" % i)
                continue

            #print("good for %s" % i)
            fulcrum = i
            break

    frankenstring_enc = s_rev_enc[:fulcrum + 1] + s_enc[1:]
    frankenstring = decode(frankenstring_enc)
    return frankenstring


if __name__ == '__main__':
    s = random.choices('abc', k=8)
    s = ''.join(s)

    print(s)
    result = solution(s)
    print(result)


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "aacecaaa"
        expecting = "aaacecaaa"
        self.assertEqual(expecting, solution(s))

    def test_2(self):
        s = "abcd"
        expecting = "dcbabcd"
        self.assertEqual(expecting, solution(s))

