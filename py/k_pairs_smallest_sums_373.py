#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(arr1, arr2, k):
    bucket = set()
    pair_to_value = {}
    value_to_pair = {}
    initial = (0, 0)
    bucket.add(initial)
    value = arr1[initial[0]] + arr2[initial[1]]
    value_to_pair[value] = [initial]
    pair_to_value[initial] = value
    result = []

    for i in range(k):
        minkey = min(value_to_pair.keys())
        pair = value_to_pair[minkey][0]

        result.append([arr1[pair[0]], arr2[pair[1]]])

        successor1 = successor2 = None
        sum1 = sum2 = None
        if pair[0] < len(arr1) - 1:
            successor1 = (pair[0] + 1, pair[1])
            sum1 = sum(arr1[successor1[0]], arr2[successor1[1]])

        if pair[1] < len(arr2) - 1:
            successor2 = (pair[0], pair[1] + 1)
            sum2 = sum(arr1[successor2[0]], arr2[successor2[1]])

        if sum1 is None and sum2 is None:
            break

        if sum1 is not None and sum2 is not None:
            if sum1 < sum2:
                bucket.add(successor1)
                value = arr1[successor1[0]] + arr2[successor1[1]]
                if value not in value_to_pair:
                    value_to_pair[value] = []
                value_to_pair[value].append(successor1)
                pair_to_value[successor1] = value
            else:
                bucket.add(successor2)
                value = arr1[successor2[0]] + arr2[successor2[1]]
                if value not in value_to_pair:
                    value_to_pair[value] = []
                value_to_pair[value].append(successor2)
                pair_to_value[successor2] = value

            del pair_to_value[pair]
            value_to_pair[minkey].pop()
            bucket.remove(pair)
            continue

        if sum1 is not None:
            bucket.add(successor1)
            value = arr1[successor1[0]] + arr2[successor1[1]]
            if value not in value_to_pair:
                value_to_pair[value] = []
            value_to_pair[value].append(successor1)
            pair_to_value[successor1] = value
        else:
            bucket.add(successor2)
            value = arr1[successor2[0]] + arr2[successor2[1]]
            if value not in value_to_pair:
                value_to_pair[value] = []
            value_to_pair[value].append(successor2)
            pair_to_value[successor2] = value

        del pair_to_value[pair]
        value_to_pair[minkey].pop()
        bucket.remove(pair)

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
