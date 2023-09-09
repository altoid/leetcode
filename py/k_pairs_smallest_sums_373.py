#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(arr1, arr2, k):
    value_to_pair = {}
    initial = (0, 0)
    value = arr1[initial[0]] + arr2[initial[1]]
    value_to_pair[value] = [initial]
    result = []
    bucket = set()
    bucket.add(initial)
    
    for i in range(k):
        if len(value_to_pair) == 0:
            break

        minkey = min(value_to_pair.keys())
        pair = value_to_pair[minkey][0]

        result.append([arr1[pair[0]], arr2[pair[1]]])

        if pair[0] < len(arr1) - 1:
            successor = (pair[0] + 1, pair[1])
            if successor not in bucket:
                value = arr1[successor[0]] + arr2[successor[1]]
                if value not in value_to_pair:
                    value_to_pair[value] = []
                value_to_pair[value].append(successor)
                bucket.add(successor)

        if pair[1] < len(arr2) - 1:
            successor = (pair[0], pair[1] + 1)
            if successor not in bucket:
                value = arr1[successor[0]] + arr2[successor[1]]
                if value not in value_to_pair:
                    value_to_pair[value] = []
                value_to_pair[value].append(successor)
                bucket.add(successor)

        value_to_pair[minkey].pop(0)
        if len(value_to_pair[minkey]) == 0:
            del value_to_pair[minkey]

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_4(self):
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 10
        expected = [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]]
        self.assertEqual(expected, solution(nums1, nums2, k))

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
