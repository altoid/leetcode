#!/usr/bin/env python

# https://leetcode.com/problems/longest-palindromic-substring/

# we will consider single chars to be palindromes.

import unittest
from pprint import pprint


def check_odd_pdrome(s, i):
    """
    find the longest odd-length palindrome whose center is i.  return i and the radius
    """
    radius = 0

    while True:
        left = i - radius
        right = i + radius

        if left < 0:
            break
        if right >= len(s):
            break

        if s[left] != s[right]:
            break

        radius += 1

    return i, radius - 1


def check_even_pdrome(s, i):
    """
    should only be called if i is not the last char in the string and s[i] == s[i + 1].
    return i and the radius.
    """

    radius = 0
    while True:
        left = i - radius
        right = i + 1 + radius

        if left < 0:
            break
        if right >= len(s):
            break

        if s[left] != s[right]:
            break

        radius += 1

    return i, radius - 1


def solution(s):
    odd_pdromes = set()
    even_pdromes = set()

    i = 0
    while i < len(s):
        tup = check_odd_pdrome(s, i)
        odd_pdromes.add(tup)

        if i < len(s) - 1 and s[i] == s[i + 1]:
            tup = check_even_pdrome(s, i)
            even_pdromes.add(tup)
        i += 1

    longest_odd_pdrome = max(odd_pdromes, key=lambda x: x[1])
    if len(even_pdromes) > 0:
        longest_even_pdrome = max(even_pdromes, key=lambda x: x[1])

        if longest_even_pdrome[1] >= longest_odd_pdrome[1]:
            left = longest_even_pdrome[0] - longest_even_pdrome[1]
            right = longest_even_pdrome[0] + longest_even_pdrome[1] + 2
        else:
            left = longest_odd_pdrome[0] - longest_odd_pdrome[1]
            right = longest_odd_pdrome[0] + longest_odd_pdrome[1] + 1
    else:
        left = longest_odd_pdrome[0] - longest_odd_pdrome[1]
        right = longest_odd_pdrome[0] + longest_odd_pdrome[1] + 1

    return s[left:right]


class Solution:
    def longestPalindrome(self, s):
        return solution(s)


if __name__ == '__main__':
    pass

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_odd_1(self):
        s = 'digit'
        result = check_odd_pdrome(s, 1)
        self.assertEqual((1, 0), result)

    def test_odd_2(self):
        s = 'digit'
        result = check_odd_pdrome(s, 2)
        self.assertEqual((2, 1), result)

    def test_even_1(self):
        s = 'abbc'
        result = check_even_pdrome(s, 1)
        self.assertEqual((1, 0), result)

    def test_solution_1(self):
        s = 'digit'
        self.assertEqual('igi', solution(s))

    def test_solution_2(self):
        s = 'abbc'
        self.assertEqual('bb', solution(s))

    def test_solution_3(self):
        s = 'u07o3j4jk2f04fxc8p8d6x8kui1ppra0j3xy85lr21y84fxyb4sqmdf'
        print(solution(s))