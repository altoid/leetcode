#!/usr/bin/env python

# https://leetcode.com/contest/weekly-contest-291/problems/total-appeal-of-a-string/

# approach:  look at every fucking substring.  use dynamic programming to keep track of substrings that we
# have already seen

import unittest
import random
from pprint import pprint

# map a string to the number of unique chars in it


class Solution:

    def __init__(self):
        self.substring_appeal = {}
        self.table = {}

    def make_table(self, text):
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
        """

        # maps unique letters to their arrays
        unique_letters = set(text)
        for letter in unique_letters:
            self.table[letter] = [0] * (1 + len(text))
            i = 1
            v = 0
            for t in text:
                if t == letter:
                    v = i
                self.table[letter][i] = v
                i += 1

        pprint(self.table)

    def count_unique_chars(self, s):
        char_counts = {}

        if s not in self.substring_appeal:

            for c in s:
                if c not in char_counts:
                    char_counts[c] = 0

                char_counts[c] += 1

            self.substring_appeal[s] = len(char_counts)

    #    print(s, substring_appeal[s])
        return self.substring_appeal[s]

    def appealSum(self, text: str) -> int:
        l = len(text)

        total = 0

        for i in range(0, l):
            for j in range(i + 1, l + 1):
                substring = text[i:j]
                total += self.count_unique_chars(substring)

        return total


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_make_table(self):
        text = 'fiddlefaddle'
        self.s.make_table(text)

    def test_count_unique_1(self):
        self.assertEqual(3, self.s.count_unique_chars('abbca'))

    def test_count_unique_2(self):
        self.assertEqual(3, self.s.count_unique_chars(''.join(random.choices('abc', k=20))))

    def test_appeal_1(self):
        self.assertEqual(28, self.s.appealSum('abbca'))

    def test_appeal_2(self):
        self.assertEqual(20, self.s.appealSum('code'))
