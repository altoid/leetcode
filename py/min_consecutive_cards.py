#!/usr/bin/env python

# https://leetcode.com/contest/weekly-contest-291/problems/minimum-consecutive-cards-to-pick-up/

import unittest
from pprint import pprint

from typing import List


class Solution:
    def __init__(self):
        self.value_to_positions = {}

    def minimumCardPickup(self, cards: List[int]) -> int:
        p = 0
        for c in cards:
            if c not in self.value_to_positions:
                self.value_to_positions[c] = []
            self.value_to_positions[c].append(p)
            p += 1

        # if the longest list of positions is 1, then no card appears more than once and they are all unique.
        lengths = map(len, self.value_to_positions.values())
        longest = max(lengths)
        if longest == 1:
            return -1

        result = len(cards)

        for k in self.value_to_positions.keys():
            a = self.value_to_positions[k]
            if len(a) == 1:
                continue

            for i in range(len(a) - 1):
                d = a[i + 1] - a[i] + 1
                result = min(d, result)

        return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_1(self):
        cards = [3, 4, 2, 3, 4, 7]
        self.assertEqual(4, self.s.minimumCardPickup(cards))

    def test_2(self):
        cards = [3, 4, 2, 7]
        self.assertEqual(-1, self.s.minimumCardPickup(cards))
