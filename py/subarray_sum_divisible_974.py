#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(nums, k):
    prefix_sums = []
    partial_sum = 0
    for i in range(len(nums)):
        partial_sum += nums[i]
        prefix_sums.append(partial_sum % k)

    prefix_sum_to_i = {}
    for i in range(len(prefix_sums)):
        if prefix_sums[i] not in prefix_sum_to_i:
            prefix_sum_to_i[prefix_sums[i]] = []
        prefix_sum_to_i[prefix_sums[i]].append(i)

    result = 0

    # print("k = %s" % k)
    # print("nums")
    # pprint(nums)
    # print("prefix_sums")
    # pprint(prefix_sums)
    # print("prefix_sum_to_i")
    # pprint(prefix_sum_to_i)

    for k, v in prefix_sum_to_i.items():
        n = len(v)
        result += (n * (n - 1)) // 2
        if k == 0:
            result += n

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_2(self):
        nums = [5]
        k = 9
        expecting = 0
        self.assertEqual(expecting, solution(nums, k))

    def test_1(self):
        nums = [4, 5, 0, -2, -3, 1]
        k = 5
        expecting = 7
        self.assertEqual(expecting, solution(nums, k))

