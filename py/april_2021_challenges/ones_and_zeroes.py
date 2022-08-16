#!/usr/bin/env python3

# https://leetcode.com/problems/ones-and-zeroes/

# evaluate # 0s and 1s in each string

import unittest


# convert to tuples
# eliminate every tuple where 0s > m or 1s > n
# see if the remainder satisfies the condition
# if it doesn't, keep removing the tuple with the biggest 0 or 1 component until it does.
#
# needs a DP solution:  remove the tuple with the largest 0 component
# and again with thet largest 1 component and see which one wins.
# proceed recursively on the results until we find a winner.

def mycmp(a, b):
    """
    a and b are two-ples
    """
    ma = max(a[0], a[1])
    mb = max(b[0], b[1])
    if ma == mb:
        return sum(a) - sum(b)
    return ma - mb


def bitstring_encode(bitstring):
    """
    return a two-ple of ints, giving # of 0s and 1s in the string
    """

    l = list(bitstring)
    ones = len([x for x in l if x == '1'])
    zeroes = len(bitstring) - ones
    return (zeroes, ones)


class Solution(object):

    def findMaxForm(self, strs, m_zeroes, n_ones):
        # threw away original solution, needs a redo
        return 0

if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    soln = Solution()
    print(soln.findMaxForm(strs, 5, 3))


class MyTest(unittest.TestCase):
    def test_bs_encode(self):
        bs = ""
        self.assertEqual((0, 0), bitstring_encode(bs))

        bs = "0"
        self.assertEqual((1, 0), bitstring_encode(bs))

        bs = "1"
        self.assertEqual((0, 1), bitstring_encode(bs))

        bs = "01"
        self.assertEqual((1, 1), bitstring_encode(bs))

        bs = "111001"
        self.assertEqual((2, 4), bitstring_encode(bs))

    def test1(self):
        soln = Solution()
        strs = ["10", "0001", "111001", "1", "0"]
        self.assertEqual(4, soln.findMaxForm(strs, 5, 3))

    def test2(self):
        soln = Solution()
        strs = ["10", "1", "0"]
        self.assertEqual(2, soln.findMaxForm(strs, 1, 1))

    def test3(self):
        soln = Solution()
        strs = ["111", "1000", "1000", "1000"]
        self.assertEqual(3, soln.findMaxForm(strs, 9, 3))
