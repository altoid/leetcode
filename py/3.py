#!/usr/bin/env python

# https://leetcode.com/problems/longest-substring-without-repeating-characters/?tab=Description

# Given a string, find the length of the longest substring without repeating characters.
# in case of a tie, earliest substring wins.

import unittest
from pprint import pprint


def solution(str):
    characters_seen = {}
    current_run = 0
    longest_run = 0
    last_repeated_char = None
    p = 0
    for c in str:
        if c not in characters_seen:
            characters_seen[c] = []
            characters_seen[c].append(p)
            current_run += 1
        else:
            # this is a character we've seen before.
            if not last_repeated_char:
                last_repeated_char = characters_seen[c][-1]
                longest_run = max(current_run, longest_run)
                current_run = p - last_repeated_char
            else:
                # if the current character last occurred earlier than the last repeated character,
                # the streak is unbroken.
                if last_repeated_char < characters_seen[c][-1]:
                    last_repeated_char = characters_seen[c][-1]
                    longest_run = max(current_run, longest_run)
                    current_run = p - last_repeated_char
                else:
                    current_run += 1
            characters_seen[c].append(p)

        p += 1

    longest_run = max(longest_run, current_run)
    
    return longest_run


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, solution("whathathgodwrought"))

    def test_2(self):
        self.assertEqual(1, solution("w"))

    def test_3(self):
        self.assertEqual(0, solution(""))

    def test_4(self):
        self.assertEqual(1, solution("wwwwwww"))

    def test_5(self):
        self.assertEqual(7, solution("abcdefg"))
