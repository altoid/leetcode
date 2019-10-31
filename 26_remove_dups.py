#!/usr/bin/env python

import unittest


class Solution(object):
    def removeDuplicates(self, arr):
        if len(arr) <= 1:
            return len(arr)

        # are we here?  then the array has at least 2 elements in it.
        current = 0
        next_value = 1
        array_len = len(arr)

        while next_value < array_len:
            while next_value < array_len and arr[current] == arr[next_value]:
                next_value += 1
            if next_value < array_len:
                current += 1
                arr[current] = arr[next_value]
                next_value += 1

        return current + 1


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_mono(self):
        arr = [1]
        result = 1
        self.assertEqual(result, self.solution.removeDuplicates(arr))
        self.assertEqual([1], arr[:result])

        arr = [1, 1]
        result = 1
        self.assertEqual(result, self.solution.removeDuplicates(arr))
        self.assertEqual([1], arr[:result])

        arr = [1, 1, 1]
        result = 1
        self.assertEqual(result, self.solution.removeDuplicates(arr))
        self.assertEqual([1], arr[:result])

    def test1(self):
        arr = [1, 1, 1, 2, 2, 3]
        control = [1, 2, 3]
        expected = len(control)
        result = self.solution.removeDuplicates(arr)
        self.assertEqual(expected, result)
        self.assertEqual(control, arr[:expected])

    def test2(self):
        arr = [0, 0, 0, 1, 1, 1, 1, 2, 3, 3]
        control = [0, 1, 2, 3]
        expected = len(control)
        result = self.solution.removeDuplicates(arr)
        self.assertEqual(expected, result)
        self.assertEqual(control, arr[:expected])

    def test_nodups(self):
        arr = [0, 1, 2, 3]
        control = [0, 1, 2, 3]
        expected = len(control)
        result = self.solution.removeDuplicates(arr)
        self.assertEqual(expected, result)
        self.assertEqual(control, arr[:expected])
