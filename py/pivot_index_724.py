#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(nums):
    total = sum(nums)
    left_sums = [0] * len(nums)
    right_sums = [0] * len(nums)

    right_sums[0] = total - nums[0]
    if right_sums[0] == left_sums[0]:
        return 0

    for i in range(1, len(nums)):
        left_sums[i] = left_sums[i - 1] + nums[i - 1]
        right_sums[i] = right_sums[i - 1] - nums[i]

        if right_sums[i] == left_sums[i]:
            return i

    return -1


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_3(self):
        nums = [2, 1, -1]
        expecting = 0
        self.assertEqual(expecting, solution(nums))

    def test_2(self):
        nums = [1, 2, 3]
        expecting = -1
        self.assertEqual(expecting, solution(nums))

    def test_1(self):
        nums = [1, 7, 3, 6, 5, 6]
        expecting = 3
        self.assertEqual(expecting, solution(nums))
