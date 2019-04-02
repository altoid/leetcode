#!/usr/bin/env python

# https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).

import unittest
import random


def find_median(arr1, arr2):
    pass


def binary_search_helper(arr, target, left, right):
    """
    return the index of the leftmost occurrence of target.  return None if target not present.

    :param arr: sorted array of ints
    :param target: what we are looking for in arr
    :param left:
    :param right:
    :return:
    """

    if right < left:
        return None

    if left == right:
        if arr[left] == target:
            return left
        return None

    m = (left + right) / 2

    if arr[m] == target:
        # wind to the left until we find the leftmost occurrence of target
        if m == 0:
            return m

        while arr[m - 1] == target:
            m = m - 1

        return m

    if target < arr[m]:
        return binary_search_helper(arr, target, left, m - 1)

    return binary_search_helper(arr, target, m + 1, right)


def binary_search(arr, target):
    return binary_search_helper(arr, target, 0, len(arr) - 1)


def generate_array():
    length = random.randint(5, 11)
    return sorted([random.randint(10, 40) for i in xrange(length)])


class TestMedian(unittest.TestCase):

    def setUp(self):
        self.basic_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # def test1(self):
    #     a = generate_array()
    #     b = generate_array()
    #
    #     if len(a) < len(b):
    #         a, b = b, a
    #
    #     print a, len(a)
    #     print b, len(b)
    #
    #     print sorted(a + b)

    def test_bsearch_1(self):
        # find something.

        result = binary_search(self.basic_arr, 2)
        self.assertEqual(1, result)

    def test_bsearch_2(self):
        # look for something bigger than anything in the array
        result = binary_search(self.basic_arr, 22)
        self.assertIsNone(result)

    def test_bsearch_3(self):
        # look for something smaller than anything in the array
        result = binary_search(self.basic_arr, 0)
        self.assertIsNone(result)

    def test_bsearch_4(self):
        # look for something that appears a bunch of times
        arr = [1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8]
        result = binary_search(arr, 2)
        self.assertEqual(1, result)

    def test_bsearch_5(self):
        arr = [1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8]
        result = binary_search(arr, 3)
        self.assertEqual(5, result)

    def test_bsearch_6(self):
        arr = [1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8]

        result = binary_search(arr, 5)
        self.assertEqual(7, result)
