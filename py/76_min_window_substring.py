#!/usr/bin/env python

# https://leetcode.com/problems/minimum-window-substring/

import unittest
from pprint import pprint
import random


def census_complete(window_census, t_chars_to_match):
    """
    return true iff every character (including dups) in t_chars_to_match is also in the window_census
    """

    # this check can be considered an O(1) operation, because checking each letter takes constant time
    # and the max number of unique letters is a constant.

    for tk, tv in t_chars_to_match.items():
        if window_census[tk] < tv:
            return False

    return True


def add_to_census(window_census, c):
    if c not in window_census:
        return

    window_census[c] += 1


def remove_from_census(window_census, c):
    if c not in window_census:
        return

    if window_census[c] == 0:
        return

    window_census[c] -= 1


def solution(s, t):
    t_chars_to_match = {}
    for c in t:
        if c not in t_chars_to_match:
            t_chars_to_match[c] = 0
        t_chars_to_match[c] += 1

    window_census = {}
    for c in t:
        if c not in window_census:
            window_census[c] = 0

    wright = wleft = 0
    shortest_window = current_window = None

    while wleft < len(s):
        while not census_complete(window_census, t_chars_to_match) and wright < len(s):
            add_to_census(window_census, s[wright])
            wright += 1

        if census_complete(window_census, t_chars_to_match):
            current_window = (wleft, wright)

        remove_from_census(window_census, s[wleft])
        wleft += 1
        while census_complete(window_census, t_chars_to_match) and wleft < len(s):
            current_window = (wleft, wright)
            remove_from_census(window_census, s[wleft])
            wleft += 1

        if current_window:
            if not shortest_window:
                shortest_window = current_window
            elif current_window[1] - current_window[0] < shortest_window[1] - shortest_window[0]:
                shortest_window = current_window

    if shortest_window:
        return s[shortest_window[0]:shortest_window[1]]
    return ""


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        w = solution(s, t)
        self.assertEqual(expected, w)

    def test_2(self):
        s = "a"
        t = "a"
        expected = "a"
        w = solution(s, t)
        self.assertEqual(expected, w)

    def test_3(self):
        s = "a"
        t = "aa"
        expected = ""
        w = solution(s, t)
        self.assertEqual(expected, w)
