#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(nums, k):
    total = sum(nums)
    if total < k:
        return - 1

    prefixes = []
    suffixes = []
    partial_sum = 0
    current_suffix = total
    prefix_to_i = {}
    suffix_to_i = {}
    i = 0
    for n in nums:
        partial_sum += n
        prefix_to_i[partial_sum] = i
        prefixes.append(partial_sum)

        suffixes.append(current_suffix)
        suffix_to_i[current_suffix] = i
        current_suffix -= n

        i += 1

    nops = len(nums) + 1

    # look for prefix that adds to k
    i = 0
    while i < len(nums) and prefixes[i] < k:
        i += 1

    if prefixes[i] == k:
        nops = min(nops, i + 1)

    # look for suffix that adds to k
    i = 0
    while i < len(nums) and suffixes[-(i + 1)] < k:
        i += 1

    if suffixes[-(i + 1)] == k:
        nops = min(nops, i + 1)

    # look for combo
    i = 0
    while i < len(nums) and prefixes[i] < k:
        if k - prefixes[i] in suffix_to_i:
            j = suffix_to_i[k - prefixes[i]]
            j = len(nums) - 1 - j
            nops = min(nops, i + j + 2)
        i += 1

    if nops <= len(nums):
        return nops

    return -1


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_3(self):
        nums = [3, 2, 20, 1, 1, 3]
        k = 10
        expecting = 5
        self.assertEqual(expecting, solution(nums, k))

    def test_2(self):
        nums = [5, 6, 7, 8, 9]
        k = 4
        expecting = -1
        self.assertEqual(expecting, solution(nums, k))

    def test_1(self):
        nums = [1, 1, 4, 2, 3]
        k = 5
        expecting = 2
        self.assertEqual(expecting, solution(nums, k))
