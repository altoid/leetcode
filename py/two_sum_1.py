#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def solution(arr, target):
    value_to_addend = {n: target - n for n in arr}

    value_to_index = {}
    for i in range(len(arr)):
        if arr[i] not in value_to_index:
            value_to_index[arr[i]] = []
        value_to_index[arr[i]].append(i)
    pprint(value_to_index)
    pprint(value_to_addend)

    for n in arr:
        if target - n in value_to_addend:
            if n != target - n:
                return [value_to_index[n][0], value_to_index[target - n][0]]

            if len(value_to_index[n]) > 1:
                return [value_to_index[n][0], value_to_index[n][1]]


if __name__ == '__main__':
    arr = [3, 2, 4]
    target = 6
    answer = solution(arr, target)
    print(answer)


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [3, 2, 4]
        target = 6
        expecting = [1, 2]
        answer = sorted(solution(arr, target))
        self.assertEqual(expecting, answer)

    def test_2(self):
        arr = [3, 3]
        target = 6
        expecting = [0, 1]
        answer = sorted(solution(arr, target))
        self.assertEqual(expecting, answer)
