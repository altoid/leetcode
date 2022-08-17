#!/usr/bin/env python

# https://leetcode.com/contest/weekly-contest-291/problems/total-appeal-of-a-string/

# approach:  look at every fucking substring.  use dynamic programming to keep track of substrings that we
# have already seen

import unittest
import random

# map a string to the number of unique chars in it


class Solution:

    def __init__(self):
        self.substring_appeal = {}

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
    s = Solution()
    print(s.appealSum('abbca'))


class MyTest(unittest.TestCase):
    def test_count_unique_1(self):
        s = Solution()
        self.assertEqual(3, s.count_unique_chars('abbca'))

    def test_count_unique_2(self):
        s = Solution()
        self.assertEqual(3, s.count_unique_chars(''.join(random.choices('abc', k=20))))

    def test_appeal_1(self):
        s = Solution()
        self.assertEqual(28, s.appealSum('abbca'))

    def test_appeal_2(self):
        s = Solution()
        self.assertEqual(20, s.appealSum('code'))
