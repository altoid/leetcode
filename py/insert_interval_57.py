#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random
from functools import reduce

# [a b] and [b c] overlap


def helper(acc, value):
    last = acc[-1]
    if value[0] > last[1]:
        acc.append(value)
    else:
        merged = [last[0], max(last[1], value[1])]
        acc.pop()
        acc.append(merged)
    #pprint(acc)
    return acc


def solution(intervals, newinterval):
    if not intervals:
        return [newinterval]

    intervals.append(newinterval)
    newlist = sorted(intervals, key=lambda x: x[0])
    #pprint(newlist)

    acc = [newlist[0]]
    result = reduce(helper, newlist[1:], acc)
    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_3(self):
        intervals = []
        newinterval = [2, 5]
        expecting = [[2, 5]]

        result = solution(intervals, newinterval)
        self.assertEqual(expecting, result)

    def test_2(self):
        intervals = [[1, 3], [6, 9]]
        newinterval = [2, 5]
        expecting = [[1, 5], [6, 9]]

        result = solution(intervals, newinterval)
        self.assertEqual(expecting, result)

    def test_1(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newinterval = [4, 8]
        expecting = [[1, 2], [3, 10], [12, 16]]

        result = solution(intervals, newinterval)
        self.assertEqual(expecting, result)
