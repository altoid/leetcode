#!/usr/bin/env python

# https://leetcode.com/problems/minimum-size-subarray-sum/

# idea:  since all numbers in the array are strictly positive, use a sliding window
# to crawl along the array.  we are looking for shortest subarray >= the target, not
# the largest subarray.

import unittest
import random
from pprint import pprint


def solution(arr, k):
    subarray_sum = arr[0]
    left = right = 0
    subarray_length = shortest_subarray_length = len(arr) + 1

    while left < len(arr):
        while subarray_sum < k and right < len(arr) - 1:
            right += 1
            subarray_sum += arr[right]

        if subarray_sum >= k:
            subarray_length = right - left + 1

        subarray_sum -= arr[left]
        left += 1
        while subarray_sum >= k and left < len(arr) - 1:
            subarray_length = right - left + 1
            subarray_sum -= arr[left]
            left += 1

        shortest_subarray_length = min(shortest_subarray_length, subarray_length)

    if shortest_subarray_length > len(arr):
        return 0
    return shortest_subarray_length


class MyTest(unittest.TestCase):
    def test1(self):
        arr = [2, 3, 1, 2, 4, 3]
        expected = 2
        self.assertEqual(expected, solution(arr, 7))

    def test2(self):
        arr = [1, 4, 4]
        expected = 1
        self.assertEqual(expected, solution(arr, 4))

    def test3(self):
        arr = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 0
        self.assertEqual(expected, solution(arr, 11))

    def test4(self):
        arr = [1, 2, 3, 4]
        expected = 4
        self.assertEqual(expected, solution(arr, 10))

    def test5(self):
        arr = [1, 2, 3, 4]
        expected = 0
        self.assertEqual(expected, solution(arr, 11))

