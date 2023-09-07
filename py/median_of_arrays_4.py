#!/usr/bin/env python

# https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).
import sys
import unittest
import random


def array_as_str(a, **kwargs):
    p = kwargs.get('partition')
    if p is not None:
        p += 1
        return "%s | %s [%s]" % (' '.join(map(str, a[:p])), ' '.join(map(str, a[p:])), simple_median(a))

    return '%s [%s]' % (' '.join(map(str, a)), simple_median(a))


def simple_median(a):
    len_a = len(a)
    m = len_a // 2
    if len_a % 2 == 1:
        return a[m]
    return (a[m - 1] + a[m]) / 2.0


def true_median(a, b):
    return simple_median(sorted(a + b))


def partition(a, b):
    """
    return the number of items in a and b that are present in the left partition of a and b.
    """
    # len(a) <= len(b)

    h = (len(a) + len(b)) // 2

    # a_left is the number of items from a that are in the left partition.  always >= 1.
    # b_left is the number of items from b that are in the left partition.  could be 0.
    a_left = (len(a) + 1) // 2
    b_left = h - a_left

    return a_left, b_left


def find_median(arr1, arr2):
    # take a to be the shorter one
    a = arr1
    b = arr2
    if len(arr2) < len(arr1):
        a, b = b, a

    if len(a) == 0:
        return simple_median(b)

    is_even = (len(a) + len(b)) % 2 == 0
    a_left, b_left = partition(a, b)

    while True:
        if a_left == 0:
            a_left_max = -sys.maxsize
            a_right_min = a[0]
        elif a_left == len(a):
            a_left_max = a[-1]
            a_right_min = sys.maxsize
        else:
            a_left_max = a[a_left - 1]
            a_right_min = a[a_left]

        if b_left == 0:
            b_left_max = -sys.maxsize
            b_right_min = b[0]
        elif b_left == len(b):
            b_left_max = b[-1]
            b_right_min = sys.maxsize
        else:
            b_left_max = b[b_left - 1]
            b_right_min = b[b_left]

        if a_left_max <= b_right_min and b_left_max <= a_right_min:
            if is_even:
                answer = (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2.0
            else:
                answer = min(a_right_min, b_right_min)

            return answer

        if a_left_max > b_right_min:
            a_left -= 1
            b_left += 1

        else:
            a_left += 1
            b_left -= 1

        assert 0 <= a_left <= len(a)
        assert 0 <= b_left <= len(b)


def generate_array():
    length = random.randint(1, 1000)
    return sorted([random.randint(10, 40) for _ in range(length)])


if __name__ == '__main__':
    while True:
        a = generate_array()
        b = generate_array()
        # print("a = %s" % a)
        # print("b = %s" % b)
        # print("a = %s" % array_as_str(a))
        # print("b = %s" % array_as_str(b))
        # print("combo = %s" % array_as_str(sorted(a + b)))
        #
        compare = true_median(a, b)
        # print("true median = %s" % compare)
        test = find_median(a, b)
        # print("exp median = %s" % test)
        assert compare == test


class TestPartition(unittest.TestCase):

    def test_partition_1(self):
        a = [1]
        b = [5]
        a_left, b_left = partition(a, b)
        self.assertEqual(1, a_left)
        self.assertEqual(0, b_left)

    def test_partition_2(self):
        a = [1]
        b = [5, 6]
        a_left, b_left = partition(a, b)
        self.assertEqual(1, a_left)
        self.assertEqual(0, b_left)

    def test_partition_3(self):
        a = [1, 2]
        b = [5, 6]
        a_left, b_left = partition(a, b)
        self.assertEqual(1, a_left)
        self.assertEqual(1, b_left)

    def test_partition_4(self):
        a = [1, 2]
        b = [5, 6, 7]
        a_left, b_left = partition(a, b)
        self.assertEqual(1, a_left)
        self.assertEqual(1, b_left)


class TestMedian(unittest.TestCase):
    def test_median_11(self):
        a = [35]
        b = []
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_10(self):
        a = [35, 36]
        b = [13, 15, 17, 18, 21]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_9(self):
        a = [5]
        b = [1]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_8(self):
        a = [1]
        b = [5]
        self.assertEqual(true_median(a, b), find_median(a, b))

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

    def test_median_6(self):
        a = [11, 11, 12, 12, 18, 22, 27, 30, 32, 33, 34, 36]
        b = [11, 15, 28, 39, 40]
        self.assertEqual(true_median(a, b), find_median(a, b))

    def test_median_7(self):
        a = [10, 24, 30, 33]
        b = [15, 19, 19, 24, 33, 33, 36, 39, 40]
        self.assertEqual(true_median(a, b), find_median(a, b))
