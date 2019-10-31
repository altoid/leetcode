#!/usr/bin/env python

import unittest

"""
notes

need the position of the first permutation with a given prefix
- when the prefix is empty, this will be 1

given this position and k, get the next element to add to the prefix

keep going until prefix is n-1 long

prefix will be values, not indexes
 
"""

class Solution(object):
    factorials = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
    }

    def my_factorial(self, n):
        return self.factorials[n]

    def roundup(self, k, n):
        """
        round up k to nearest multiple of n

        :param k:
        :param n:
        :return:
        """
        return ((k + (n - 1)) / n) * n

    def howmany(self, k, n):
        """
        how many intervals of size n are covered by k?

        :param k:
        :param n:
        :return:
        """
        return (k + (n - 1)) / n

    def first_with_prefix(self, prefix, arr):
        result = 1

        arr_copy = list(arr)
        for p in prefix:
            n = len(arr_copy)
            i = arr_copy.index(p)
            result += i * self.my_factorial(n - 1)
            arr_copy.pop(i)

        return result

    def get_next_element(self, prefix, k, arr):
        # arr is the whole list of values.  copy it and remove the prefix elements from it

        if len(prefix) < len(arr):
            arr_copy = list(arr)
            for p in prefix:
                arr_copy.remove(p)

            first = self.first_with_prefix(prefix, arr)
            window = self.my_factorial(len(arr_copy) - 1)
            h = self.howmany(k - first + 1, window)
            element = arr_copy[h - 1]
            return element

    def getPermutation(self, n, k):
        """

        :param n: length of sequence (we don't get the array)
        :param k: produce the kth permutation
        :return: permutation, as a string
        """
        a = [x + 1 for x in xrange(n)]
        prefix = []

        e = self.get_next_element(prefix, k, a)
        while e is not None:
            prefix.append(e)
            e = self.get_next_element(prefix, k, a)

        return prefix


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_roundup(self):
        self.assertEqual(0, self.solution.roundup(0, 5))
        self.assertEqual(5, self.solution.roundup(1, 5))
        self.assertEqual(5, self.solution.roundup(2, 5))
        self.assertEqual(5, self.solution.roundup(3, 5))
        self.assertEqual(5, self.solution.roundup(4, 5))
        self.assertEqual(5, self.solution.roundup(5, 5))
        self.assertEqual(10, self.solution.roundup(6, 5))
        self.assertEqual(10, self.solution.roundup(7, 5))
        self.assertEqual(15, self.solution.roundup(11, 5))

    def test_howmany(self):
        self.assertEqual(0, self.solution.howmany(0, 5))
        self.assertEqual(1, self.solution.howmany(1, 5))
        self.assertEqual(1, self.solution.howmany(2, 5))
        self.assertEqual(1, self.solution.howmany(3, 5))
        self.assertEqual(1, self.solution.howmany(4, 5))
        self.assertEqual(1, self.solution.howmany(5, 5))
        self.assertEqual(2, self.solution.howmany(6, 5))
        self.assertEqual(2, self.solution.howmany(7, 5))
        self.assertEqual(3, self.solution.howmany(11, 5))
        self.assertEqual(8, self.solution.howmany(36, 5))

    def test_first_with_prefix(self):
        n = 5
        a = [x + 1 for x in xrange(n)]

        self.assertEqual(1, self.solution.first_with_prefix([], a))
        self.assertEqual(1, self.solution.first_with_prefix([1], a))
        self.assertEqual(25, self.solution.first_with_prefix([2], a))
        self.assertEqual(49, self.solution.first_with_prefix([3], a))

        self.assertEqual(49, self.solution.first_with_prefix([3, 1], a))
        self.assertEqual(55, self.solution.first_with_prefix([3, 2], a))
        self.assertEqual(55, self.solution.first_with_prefix([3, 2, 1], a))
        self.assertEqual(57, self.solution.first_with_prefix([3, 2, 4], a))
        self.assertEqual(57, self.solution.first_with_prefix([3, 2, 4, 1], a))
        self.assertEqual(58, self.solution.first_with_prefix([3, 2, 4, 5], a))
        self.assertEqual(58, self.solution.first_with_prefix([3, 2, 4, 5, 1], a))

        self.assertEqual(59, self.solution.first_with_prefix([3, 2, 5], a))

    def test_get_next_element(self):
        n = 5
        a = [x + 1 for x in xrange(n)]

        self.assertEqual(1, self.solution.get_next_element([], 1, a))
        self.assertEqual(1, self.solution.get_next_element([], 23, a))
        self.assertEqual(1, self.solution.get_next_element([], 24, a))
        self.assertEqual(2, self.solution.get_next_element([], 25, a))
        self.assertEqual(4, self.solution.get_next_element([], 73, a))
        self.assertEqual(5, self.solution.get_next_element([], 120, a))

        self.assertEqual(3, self.solution.get_next_element([], 57, a))
        self.assertEqual(2, self.solution.get_next_element([3], 57, a))
        self.assertEqual(4, self.solution.get_next_element([3, 2], 57, a))
        self.assertEqual(1, self.solution.get_next_element([3, 2, 4], 57, a))
        self.assertEqual(5, self.solution.get_next_element([3, 2, 4, 1], 57, a))
        self.assertIsNone(self.solution.get_next_element([3, 2, 4, 1, 5], 57, a))

        self.assertIsNone(self.solution.get_next_element([1, 2, 3, 4, 5], 57, a))

    def test_examples(self):
        self.assertEqual([2, 1, 3], self.solution.getPermutation(3, 3))
        self.assertEqual([2, 3, 1, 4], self.solution.getPermutation(4, 9))
