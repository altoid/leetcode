#!/usr/bin/env python

# https://leetcode.com/contest/weekly-contest-291/problems/total-appeal-of-a-string/

# approach:  look at every fucking substring.  use dynamic programming to keep track of substrings that we
# have already seen

import unittest
import random
from pprint import pprint

# map a string to the number of unique chars in it


class Solution:

    def appealSum(self, text):
        """
        for each unique letter in the text, create an array.  the length is 1 + len(text).  initialized to all
        zeroes.  the values in a letter's array are the index (1 based) of the last appearance at or before i.

        this could also be interpreted as the number of substrings containing that letter which end at that position.
        example:

        text:  fiddlefaddle

        letters:  adefil

                f  i  d  d  l  e  f  a  d  d  l  e
             0  1  2  3  4  5  6  7  8  9 10 11 12

        a:   0  0  0  0  0  0  0  0  8  8  8  8  8
        d:   0  0  0  3  4  4  4  4  4  9 10 10 10
        e:   0  0  0  0  0  0  6  6  6  6  6  6 12
        f:   0  1  1  1  1  1  1  7  7  7  7  7  7
        i:   0  0  2  2  2  2  2  2  2  2  2  2  2
        l:   0  0  0  0  0  5  5  5  5  5  5 11 11

        the answer is the sum of all of the numbers in the table.

        UPDATE:  changed code to compute the answer this way but without using the table.
        """

        unique_letters = set(text)
        total = 0
        for letter in unique_letters:
            i = 1
            v = 0
            for t in text:
                if t == letter:
                    v = i
                total += v
                i += 1

        return total


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_appeal_1(self):
        self.assertEqual(28, self.s.appealSum('abbca'))
        self.assertEqual(20, self.s.appealSum('code'))
        self.assertEqual(272, self.s.appealSum('fiddlefaddle'))
