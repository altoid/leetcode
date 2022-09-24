#!/usr/bin/env python

# https://leetcode.com/problems/sliding-window-maximum/

import unittest
from pprint import pprint
import random
from collections import deque


def solution_bruteforce(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        result.append(max(arr[i:i + k]))
    return result


def put_in_deque(d, pair):
    if len(d) == 0:
        d.append(pair)
    elif pair[1] >= d[-1][1]:
        d.append(pair)
    else:
        while d[0][1] < pair[1]:
            d.popleft()
        d.appendleft(pair)


def solution_deque(arr, k):
    d = deque()
    result = []
    arr_enumerated = list(enumerate(arr))  # (i, v)

    for i in range(k):
        put_in_deque(d, arr_enumerated[i])
    result.append(d[-1][1])

    for i in range(k, len(arr_enumerated)):
        try:
            d.remove((i - k, arr_enumerated[i - k][1]))
        except ValueError:
            pass

        put_in_deque(d, arr_enumerated[i])
        result.append(d[-1][1])

    return result


if __name__ == '__main__':
    # arr = [1, 3, -1, -3, 2, 3, 6, 7]

    i = 1
    while True:
        arr = [random.randint(-10000, 10000) for _ in range(1, 10 ** 2)]
        k = random.randint(1, len(arr) - 1)
        deque_result = solution_deque(arr, k)
        bf_result = solution_bruteforce(arr, k)

        if bf_result != deque_result:
            print("arr = %s" % arr)
            print("k = %s" % k)
            print("expecting = %s" % bf_result)
            print("test = %s" % deque_result)
            break

        if i % 1000 == 0:
            print("ran %s tests" % i)

        i += 1


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [8, 4, 9, 1, 1, -1, -2, -1]
        k = 3
        expecting = [9, 9, 9, 1, 1, -1]
        self.assertEqual(expecting, solution_deque(arr, k))

    def test_2(self):
        arr = [10, 8, 9, 2, 8, -5, -1, -3]
        k = 5
        expecting = [10, 9, 9, 8]
        self.assertEqual(expecting, solution_deque(arr, k))

    def test_3(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        k = 4
        expecting = [10, 9, 8, 7, 6, 5, 4]
        self.assertEqual(expecting, solution_deque(arr, k))

# chokes on: [10000 .. -10000], 10007
