#!/usr/bin/env python

import unittest


class Solution(object):
    def __init__(self):
        self.cache = {}

    def ways_to_decode(self, s):
        if s not in self.cache:
            result = self.ways_to_decode_raw(s)
            self.cache[s] = result

        return self.cache[s]

    def ways_to_decode_raw(self, s):
        if not s:
            return 0

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            n = int(s)
            if n in [10, 20]:
                return 1

            if n % 10 == 0:
                return 0

            if n <= 26:
                return 2

            return 1

        prefix_2 = int(s[:2])

        if prefix_2 in [10, 20]:
            return self.ways_to_decode(s[2:])

        if prefix_2 % 10 == 0:
            return 0

        if prefix_2 <= 26:
            return self.ways_to_decode(s[1:]) + self.ways_to_decode(s[2:])

        #raise Exception("missed something")
        return self.ways_to_decode(s[1:])

    def numDecodings(self, s):
        return self.ways_to_decode(s)


class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(2, self.solution.numDecodings('12'))
        self.assertEqual(1, self.solution.numDecodings('10'))
        self.assertEqual(0, self.solution.numDecodings('30'))

    def test_2(self):
        self.assertEqual(0, self.solution.numDecodings('230'))
        self.assertEqual(3, self.solution.numDecodings('226'))

    def test_3(self):
        self.assertEqual(1, self.solution.numDecodings('110'))

    def test_4(self):
        self.assertEqual(0, self.solution.numDecodings('301'))

    def test_5(self):
        self.assertEqual(2, self.solution.numDecodings('611'))

    def test_6(self):
        print self.solution.numDecodings('12131415')

