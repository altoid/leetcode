#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


# idea:  create two arrays:
#
# - l1[i] = the number of consecutive items preceding security[i] that are >= to it
# - l2[i] = the number of consecutive items following security[i] that are >= to it


def solution(security, time):
    if time == 0:
        return [x for x in range(len(security))]

    predecessors = [0] * len(security)
    for i in range(1, len(security)):
        if security[i - 1] >= security[i]:
            predecessors[i] = predecessors[i - 1] + 1
        else:
            predecessors[i] = 0

    successors = [0] * len(security)
    for i in range(-2, -(len(security) + 1), -1):
        if security[i + 1] >= security[i]:
            successors[i] = successors[i + 1] + 1
        else:
            successors[i] = 0

    result = []
    for i in range(len(security)):
        if predecessors[i] >= time and successors[i] >= time:
            result.append(i)

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        security = [5, 3, 3, 3, 5, 6, 2]
        time = 2
        expecting = {2, 3}
        result = set(solution(security, time))
        self.assertEqual(expecting, result)

    def test_2(self):
        security = [1, 1, 1, 1, 1]
        time = 0
        expecting = {0, 1, 2, 3, 4}
        result = set(solution(security, time))
        self.assertEqual(expecting, result)

    def test_3(self):
        security = [1, 2, 3, 4, 5, 6]
        time = 2
        expecting = set()
        result = set(solution(security, time))
        self.assertEqual(expecting, result)
