#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(nums, p):
    if not nums:
        return -1

    sigma = sum(nums)
    if sigma == 0:
        return -1

    if sigma < p:
        return -1

    r = sigma % p

    if r == 0:
        return 0

    # sums[i] = sum(nums[:i+1]) % p
    sums = []
    partial_sum = 0
    for i in range(len(nums)):
        partial_sum += nums[i]
        sums.append(partial_sum % p)

    pprint(nums)
    pprint(sums)

    # diffs[i] = sums[i] - r % p
    # i.e. what we have to subtract from sums[i] to get r mod p
    diffs = []
    for i in range(len(sums)):
        diffs.append((sums[i] - r) % p)
    pprint(diffs)

    # map each of sums[i] to their indexes
    # for each sums[i], see if there is a diff that precedes it
    partial_sums_to_i = {v: k for k, v in enumerate(sums)}
    pprint(partial_sums_to_i)

    sums_to_complements = dict(zip(sums, diffs))
    pprint(sums_to_complements)

    result = len(nums) + 1
    for s in sums:
        # see if the complement of s exists
        s_complement = sums_to_complements[s]
        if s_complement not in partial_sums_to_i:
            continue

        s_i = partial_sums_to_i[s]
        c_i = partial_sums_to_i[s_complement]

        if s_i > c_i:
            result = min(result, s_i - c_i)

    if result > len(nums):
        return -1
    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        nums = [26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3]
        p = 26
        expecting = 3
        self.assertEqual(expecting, solution(nums, p))
