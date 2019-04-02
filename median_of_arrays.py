#!/usr/bin/env python

# https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).

import unittest
import random

def find_median(arr1, arr2):
    pass

def generate_array():
    len = random.randint(5, 11)
    return sorted([random.randint(10, 40) for i in xrange(len)])

class TestMedian(unittest.TestCase):

    def test1(self):
        a = generate_array()
        b = generate_array()

        if len(a) < len(b):
            a, b = b, a

        print a, len(a)
        print b, len(b)

        print sorted(a + b)
        
if __name__ == '__main__':
    unittest.main()
