#!/usr/bin/env python

# https://leetcode.com/problems/sliding-window-maximum/

import unittest
from pprint import pprint
import random
from collections import deque


def solution_bruteforce(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        result.append(max(arr[i:i+k]))
    return result


def put_in_deque(d, n):
    if len(d) == 0:
        d.append(n)
    elif n >= d[-1]:
        d.append(n)
    else:
        while d[0] < n:
            d.popleft()
        d.appendleft(n)


def solution_deque(arr, k):
    d = deque()
    result = []

    for i in range(k):
        put_in_deque(d, arr[i])
    result.append(d[-1])

    for i in range(k, len(arr)):
        if arr[i - k] == d[-1]:
            d.pop()
        put_in_deque(d, arr[i])
        result.append(d[-1])

    return result

if __name__ == '__main__':
    # arr = [1, 3, -1, -3, 2, 3, 6, 7]

    arr = [random.randint(-5, 10) for _ in range(8)]
    k = random.randint(1, len(arr) - 1)
    deque_result = solution_deque(arr, k)
    bf_result = solution_bruteforce(arr, k)

    print("arr = %s" % arr)
    print("k = %s" % k)
    print("test = %s" % deque_result)
    print("expecting = %s" % bf_result)


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [8, 4, 9, 1, 1, -1, -2, -1]
        k = 3
        expecting = [9, 9, 9, 1, 1, -1]
        self.assertEqual(expecting, solution_deque(arr, k))
