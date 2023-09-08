#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(arr1, arr2, k):
    c1, c2 = 0, 0
    k = min(k, len(arr1) * len(arr2))
    result = [[arr1[c1], arr2[c2]]]
    for i in range(k):
        if c1 == len(arr1) and c2 == len(arr2):
            break

        if c1 < len(arr1) - 1:
            p1 = [arr1[c1 + 1], arr2[c2]]
        else:
            p1 = None

        if c2 < len(arr2) - 1:
            p2 = [arr1[c1], arr2[c2 + 1]]
        else:
            p2 = None

        if p1 and p2:
            if sum(p1) < sum(p2):
                result.append(p1)
                c1 += 1
            else:
                result.append(p2)
                c2 += 1
            continue

        if p1:
            result.append(p1)
            c1 += 1
        elif p2:
            result.append(p2)
            c2 += 1

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_3(self):
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3
        expected = [[1, 2], [1, 4], [1, 6]]
        self.assertEqual(expected, solution(nums1, nums2, k))

    def test_2(self):
        nums1 = [1]
        nums2 = [3]
        k = 3
        expected = [[1, 3]]
        self.assertEqual(expected, solution(nums1, nums2, k))

    def test_1(self):
        nums1 = [1, 2]
        nums2 = [3]
        k = 3
        expected = [[1, 3], [2, 3]]
        self.assertEqual(expected, solution(nums1, nums2, k))
