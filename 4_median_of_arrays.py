#!/usr/bin/env python

# https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).

from __future__ import division

import unittest
import random


def find_median(arr1, arr2):
    # take a to be the longer one
    a = arr1
    b = arr2
    if len(arr2) > len(arr1):
        a, b = b, a

    paritya = len(a) % 2
    parityb = len(b) % 2
    if paritya != 0 or parityb != 0:
        raise Exception("fuck you")

    partitiona = len(a) // 2
    partitionb = len(b) // 2

    print
    print a
    print b
    print a[0 : partitiona], a[partitiona:]
    print b[0 : partitionb], b[partitionb:]

    aleft = a[partitiona - 1]
    bleft = b[partitionb - 1]
    aright = a[partitiona]
    bright = b[partitiona]

    leftmax = max(aleft, bleft)
    rightmin = min(aright, bright)
    print aleft, bleft
    print aright, bright
    print leftmax, rightmin
    amedian = test_median(a)
    bmedian = test_median(b)

    print amedian, bmedian

    # focus on b because it's shorter.  if bright <= aright, look in the right part of b
    # for the smallest value bigger than the smallest median.
    # if bright > aright, look in the left part of be for the smallest value bigger than the smallest median.



def test_median(arr):
    # arr does not have to be sorted
    sorted_arr = sorted(arr)
    m = len(sorted_arr) // 2

    if len(sorted_arr) % 2 == 1:
        return sorted_arr[m]

    return (sorted_arr[m] + sorted_arr[m - 1]) / 2


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
        raise Exception("NFC 0:  %s, %s, (%s, %s)" % (target, arr, left, right))

    if left == right:
        if arr[left] == target:
            return left
        return None

    m = (left + right) // 2

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


def squishy_binary_search_helper(arr, target, left, right):
    # precondition:  target is <= the largest element in the array.
    # i.e. something in the array is >= target.

    if right < left:
        # if we are here, then the target is not present in the array.
        raise Exception("NFC 1:  %s, %s, (%s, %s)" % (target, arr, left, right))

    if left == right:
        if arr[left] == target:
            return left

        for l in xrange(left, len(arr)):
            if arr[l] >= target:
                return l
        raise Exception("NFC 2:  %s, %s, (%s, %s)" % (target, arr, left, right))

    m = (left + right) // 2

    if arr[m] == target:
        # wind to the left until we find the leftmost occurrence of target
        if m == 0:
            return m

        while arr[m - 1] == target:
            m = m - 1

        return m

    if target < arr[m]:
        return squishy_binary_search_helper(arr, target, left, m - 1)

    return squishy_binary_search_helper(arr, target, m + 1, right)


def squishy_binary_search(arr, target):
    """
    return the index of the smallest array element >= target.

    returns None if the array is empty
    or if the target is bigger than anything in the array.

    :param arr:
    :param target:
    :return:
    """

    if not arr:
        return None

    if target > arr[-1]:
        return None

    return squishy_binary_search_helper(arr, target, 0, len(arr) - 1)


def generate_array():
    length = random.randint(3, 7) * 2
    return sorted([random.randint(10, 40) for i in xrange(length)])


class TestMedian(unittest.TestCase):

    def setUp(self):
        self.basic_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test1(self):
        a = generate_array()
        b = generate_array()

        find_median(a, b)

    def test2(selfs):
        a = [14, 18, 18, 23, 27, 27, 34, 38, 39, 40]
        b = [14, 17, 19, 20, 22, 28, 28, 31]

        find_median(a, b)

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

    def test_squishy_search_01(self):
        arr = []
        result = squishy_binary_search(arr, 5)
        self.assertIsNone(result)

    def test_squishy_search_02(self):
        arr = [1, 2, 3, 4, 5]
        result = squishy_binary_search(arr, 6)
        self.assertIsNone(result)

    def test_squishy_search_03(self):
        arr = [5, 6, 7, 8, 9]
        result = squishy_binary_search(arr, 7)
        self.assertEqual(2, result)

    def test_squishy_search_04(self):
        arr = [5, 6, 7, 7, 7, 7, 8, 9]
        result = squishy_binary_search(arr, 7)
        self.assertEqual(2, result)

    def test_squishy_search_05(self):
        arr = [5, 6, 7, 7, 7, 7, 8, 9]
        result = squishy_binary_search(arr, 8)
        self.assertEqual(6, result)

    def test_squishy_search_06(self):
        arr = [5, 6, 7, 8, 9, 11, 12, 13, 14]
        result = squishy_binary_search(arr, 10)
        self.assertEqual(5, result)

    def test_squishy_search_07(self):
        arr = [5, 6, 7, 8, 9, 11, 12, 13, 14]
        result = squishy_binary_search(arr, 0)
        self.assertEqual(0, result)

    def test_squishy_search_08(self):
        arr = [9, 11]
        result = squishy_binary_search(arr, 10)
        self.assertEqual(1, result)

    def test_squishy_search_09(self):
        arr = [5, 9, 9, 9, 9, 9, 12]
        result = squishy_binary_search(arr, 10)
        self.assertEqual(6, result)

    def test_squishy_search_10(self):
        arr = [5, 9, 9, 9, 9, 9, 9, 12]
        result = squishy_binary_search(arr, 10)
        self.assertEqual(7, result)

    def test_squishy_search_11(self):
        arr = [5, 9, 9, 9, 9, 9, 12]
        result = squishy_binary_search(arr, 6)
        self.assertEqual(1, result)

    def test_squishy_search_12(self):
        arr = [5, 6, 7, 8, 9, 11, 12, 13, 14]
        result = squishy_binary_search(arr, 14)
        self.assertEqual(8, result)

