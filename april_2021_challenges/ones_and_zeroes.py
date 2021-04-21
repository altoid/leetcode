#!/usr/bin/env python

# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3694/

# evaluate # 0s and 1s in each string

import unittest

# convert to tuples
# eliminate every tuple where 0s > m or 1s > n
# see if the remainder satisfies the condition
# if it doesn't, keep removing the tuple with the biggest 0 or 1 component until it does.

def bitstring_encode(bitstring):
    """
    return a two-ple of ints, giving # of 0s and 1s in the string
    """

    l = list(bitstring)
    ones = len([x for x in l if x == '1'])
    zeroes = len(bitstring) - ones
    return (zeroes, ones)

def mycmp(a, b):
    """
    a and b are two-ples
    """
    ma = max(a[0], a[1])
    mb = max(b[0], b[1])
    if ma == mb:
        return sum(a) - sum(b)
    return ma - mb

def solution(strs, m_zeroes, n_ones):
    encoded = map(bitstring_encode, strs)
    encoded = [x for x in encoded if x[0] <= m_zeroes and x[1] <= n_ones]

    # sort by the biggest component of the tuple
    encoded = sorted(encoded, cmp=mycmp)
    
    print encoded

    m, n = sum([x[0] for x in encoded]), sum([x[1] for x in encoded])
    while m > m_zeroes or n > n_ones:
        last = encoded.pop()
        m -= last[0]
        n -= last[1]

    return len(encoded)

if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    solution(strs, 5, 3)
    
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
        strs = ["10", "0001", "111001", "1", "0"]
        self.assertEqual(4, solution(strs, 5, 3))

    def test2(self):
        strs = ["10", "1", "0"]
        self.assertEqual(2, solution(strs, 1, 1))

