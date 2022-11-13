#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random

# idea:  for each index in the string we maintain a 5-bit vector, one for each vowel.
# the vowel's bit is 0 if the number of times that vowel appears an even number of times
# at or before that index; 1 otherwise.
#
# then we tally the indexes where that bit vector appears.  the biggest difference in indexes for any
# bit vector is the answer.

import string


def mine(s):
    if not s:
        return 0

    bitz = [0] * len(s)
    A = 1
    E = 2
    I = 4
    O = 8
    U = 16

    masks = {k: 0 for k in string.ascii_lowercase}
    masks['a'] = A
    masks['e'] = E
    masks['i'] = I
    masks['o'] = O
    masks['u'] = U

    bitz[0] = masks[s[0]]
    i = 1
    for c in s[1:]:
        bitz[i] = bitz[i - 1] ^ masks[c]
        i += 1

    #pprint(list(zip(s, bitz, range(len(bitz)))))

    longest = 0
    first_appearance = {}
    for i in range(len(s)):
        run = 0
        if bitz[i] == 0:
            run = i + 1
        else:
            if bitz[i] not in first_appearance:
                first_appearance[bitz[i]] = i
            run = i - first_appearance[bitz[i]]
        longest = max(longest, run)

    return longest


def solution(s):
    return mine(s)


if __name__ == '__main__':
    solution("whatever")
    pass


class MyTest(unittest.TestCase):
    def test_17(self):
        s = "aaaaaaaa"
        expecting = 8
        self.assertEqual(expecting, solution(s))

    def test_16(self):
        s = "aaaaaaa"
        expecting = 6
        self.assertEqual(expecting, solution(s))

    def test_15(self):
        s = "aoeuiaoeui"
        expecting = 10
        self.assertEqual(expecting, solution(s))

    def test_14(self):
        s = "aoeuixxxaoeui"
        expecting = 13
        self.assertEqual(expecting, solution(s))

    def test_13(self):
        s = "xaeiouxaeioux"
        expecting = 13
        self.assertEqual(expecting, solution(s))

    def test_12(self):
        s = "xxxxaoeuxxxx"
        expecting = 4
        self.assertEqual(expecting, solution(s))

    def test_11(self):
        s = "uxxxxaaaaxxx"
        expecting = 11
        self.assertEqual(expecting, solution(s))

    def test_10(self):
        s = "aaaaxxxaaaae"
        expecting = 11
        self.assertEqual(expecting, solution(s))

    def test_9(self):
        s = "xxxxaaaaxxx"
        expecting = 11
        self.assertEqual(expecting, solution(s))

    def test_8(self):
        s = "a"
        expecting = 0
        self.assertEqual(expecting, solution(s))

    def test_7(self):
        s = "x"
        expecting = 1
        self.assertEqual(expecting, solution(s))

    def test_6(self):
        s = ""
        expecting = 0
        self.assertEqual(expecting, solution(s))

    def test_5(self):
        s = "amntyyaw"
        expecting = 8
        self.assertEqual(expecting, solution(s))

    def test_4(self):
        s = "whatever"
        expecting = 5
        self.assertEqual(expecting, solution(s))

    def test_1(self):
        s = "eleetminicoworoep"
        expecting = 13
        self.assertEqual(expecting, solution(s))

    def test_2(self):
        s = "bcbcbc"
        expecting = 6
        self.assertEqual(expecting, solution(s))

    def test_3(self):
        s = "leetcodeisgreat"
        expecting = 5
        self.assertEqual(expecting, solution(s))
