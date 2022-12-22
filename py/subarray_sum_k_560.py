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
        prefix_sums.append(partial_sum)

    prefix_sum_to_i = {}
    for i in range(len(prefix_sums)):
        if prefix_sums[i] not in prefix_sum_to_i:
            prefix_sum_to_i[prefix_sums[i]] = []
        prefix_sum_to_i[prefix_sums[i]].append(i)

    additive_inverses = {s: s - k for s in prefix_sums}

    result = 0

    #pprint(prefix_sum_to_i)
    #pprint(prefix_sums)
    #pprint(additive_inverses)

    if k == 0:
        for k, v in prefix_sum_to_i.items():
            n = len(v)
            result += (n * (n - 1)) // 2
            if k == 0:
                result += n
    else:
        for i in range(len(prefix_sums)):
            inv = additive_inverses[prefix_sums[i]]
            if inv in prefix_sum_to_i:
                candidates = prefix_sum_to_i[inv]
                candidates = list(filter(lambda x: x < i, candidates))
                result += len(candidates)
            if prefix_sums[i] == k:
                result += 1

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
        k = 0
        print(solution(nums, k))
