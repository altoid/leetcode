#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(nums, k):
    if not nums:
        return False
    if len(nums) < 2:
        return False
    if k == 1:
        return True

    prefix_sums = []
    prefix_to_i = {}
    i = 0
    partial_sum = 0
    for n in nums:
        partial_sum += n
        partial_sum %= k
        prefix_sums.append(partial_sum)

        if partial_sum not in prefix_to_i:
            prefix_to_i[partial_sum] = []
        prefix_to_i[partial_sum].append(i)

        i += 1

    for i in range(len(prefix_sums)):
        if i > 0 and prefix_sums[i] == 0:
            return True
        idx = prefix_to_i[prefix_sums[i]]
        candidates = list(filter(lambda x: x <= i - 2, idx))
        if len(candidates) > 0:
            return True

    return False


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_4(self):
        nums = [2, 4, 3]
        k = 6
        expecting = True
        self.assertEqual(expecting, solution(nums, k))

    def test_3(self):
        nums = [23, 2, 6, 4, 7]
        k = 13
        expecting = False
        self.assertEqual(expecting, solution(nums, k))

    def test_2(self):
        nums = [23, 2, 6, 4, 7]
        k = 6
        expecting = True
        self.assertEqual(expecting, solution(nums, k))

    def test_1(self):
        nums = [23, 2, 4, 6, 7]
        k = 6
        expecting = True
        self.assertEqual(expecting, solution(nums, k))
