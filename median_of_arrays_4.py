#!/usr/bin/env python

# https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).

from __future__ import division

import unittest
import random
from binary_search import binary_search


def simple_median(a):
    len_a = len(a)
    m = len_a // 2
    if len_a % 2 == 1:
        return a[m]
    return (a[m - 1] + a[m]) / 2.0


def true_median(a, b):
    return simple_median(sorted(a + b))


def array_as_str(a, **kwargs):
    p = kwargs.get('partition')
    if p is not None:
        p += 1
        return "%s | %s [%s]" % (' '.join(map(str, a[:p])), ' '.join(map(str, a[p:])), simple_median(a))

    return '%s [%s]' % (' '.join(map(str, a)), simple_median(a))


def partition(a):
    p = len(a) // 2
    if len(a) % 2 == 0:
        p -= 1
    return p


def adjust(a, partition_a, median_a, b, partition_b, median_b):
    # b is the shorter array
    if median_b > median_a:
        # binary search in the left part of b for the leftmost occurrence of the largest value
        # that is <= the median
        new_part_b = binary_search.search_largest_less_than(b[:(partition_b + 1)], median_b)
        if new_part_b is None:
            # oh, boy.  if we can't locate this value then the partition is already 0.  instead
            # we have to move partition_a to the right by half the length of b.
            print "######################################"
            new_part_a = partition_a + len(b) // 2
            return new_part_a, new_part_b

        new_part_b -= 1  # since the search gave us the left endpoint of the right part
    else:
        # binary search in the right part of b for the rightmost occurrence of the smallest value that is >= the median
        new_part_b = binary_search.search_smallest_greater_than(b[(partition_b + 1):], median_b)
        new_part_b += (partition_b + 1)  # add back the true index of the median

    delta = new_part_b - partition_b

    new_part_a = partition_a - delta
    return new_part_a, new_part_b


def find_median(arr1, arr2):
    # take a to be the longer one
    a = arr1
    b = arr2
    if len(arr2) > len(arr1):
        a, b = b, a

    median_a = simple_median(a)
    median_b = simple_median(b)

    parity_len_a = len(a) % 2
    parity_len_b = len(b) % 2

    # partition_x is the rightmost index of the left partition
    partition_a = partition(a)
    partition_b = partition(b)

    left_size = partition_a + partition_b + 2
    right_size = len(a) + len(b) - left_size

    print "left_size = %s, right_size = %s" % (left_size, right_size)

    # if the array with the larger median is odd length, subtract 1 from the partition
    if median_b > median_a:
        if parity_len_b == 1 and right_size - left_size > 1:
            partition_b -= 1
    if median_a > median_b:
        if parity_len_a == 1 and right_size - left_size > 1:
            partition_a -= 1

    print array_as_str(sorted(a + b))

    print array_as_str(a, partition=partition_a)
    print array_as_str(b, partition=partition_b)

    left_max = max(a[partition_a], b[partition_b])
    right_min = min(a[partition_a + 1], b[partition_b + 1])

    while left_max > right_min:
        partition_a, partition_b = adjust(a, partition_a, median_a, b, partition_b, median_b)

        print array_as_str(a, partition=partition_a)
        print array_as_str(b, partition=partition_b)

        left_max = max(a[partition_a], b[partition_b])
        right_min = min(a[partition_a + 1], b[partition_b + 1])

    if parity_len_a != parity_len_b:
        result = left_max
    else:
        result = (left_max + right_min) / 2.0

    return result


def generate_array():
    length = random.randint(2, 15)
    return sorted([random.randint(10, 40) for _ in xrange(length)])


def print_test_case():
    a = map(str, generate_array())
    b = map(str, generate_array())
    print ' '.join(a)
    print ' '.join(b)
    print ' '.join(sorted(a + b))


if __name__ == '__main__':
    a = generate_array()
    b = generate_array()
    print "a = %s" % a
    print "b = %s" % b
    print "a = %s" % array_as_str(a)
    print "b = %s" % array_as_str(b)
    print "combo = %s" % array_as_str(sorted(a + b))

    result = find_median(a, b)
    compare = true_median(a, b)
    print "found median = %s" % result
    print "true median = %s" % compare


class TestMedian(unittest.TestCase):

    def test_partition(self):
        a = [1, 2, 3, 4, 5]
        p = partition(a)
        self.assertEqual(p, 2)

        a = [1, 2, 3, 4, 5, 6]
        p = partition(a)
        self.assertEqual(p, 2)

    def test_median_1(self):
        a = [14, 16, 20, 21, 27, 29, 37, 38]
        b = [13, 17, 21, 22, 23, 29, 31, 31, 32, 35, 35]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_2(self):
        a = [13, 15, 17, 18, 21, 31, 31, 32, 32, 32, 33, 33, 34, 39, 40]
        b = [35, 35]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_3(self):
        a = [10, 14, 15, 19, 20, 26, 26, 26, 28, 28, 29, 29, 32, 35, 38]
        b = [12, 18, 19, 34]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_4(self):
        a = [10, 18, 18, 19, 21, 22, 23, 23, 23, 28, 30, 32, 33]
        b = [15, 23, 26, 27, 28, 30, 32, 38, 40]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_5(self):
        a = [11, 14, 17, 17, 17, 18, 18, 19, 21, 23, 29, 33, 34, 39, 40]
        b = [10, 11, 21, 22, 23, 23, 26, 28, 30, 31, 34, 35, 37, 39, 39]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_5(self):
        a = [11, 11, 12, 12, 18, 22, 27, 30, 32, 33, 34, 36]
        b = [11, 15, 28, 39, 40]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_6(self):
        a = [10, 24, 30, 33]
        b = [15, 19, 19, 24, 33, 33, 36, 39, 40]
        self.assertEqual(true_median(a, b), find_median(a, b))
