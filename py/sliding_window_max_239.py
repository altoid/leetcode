#!/usr/bin/env python

# https://leetcode.com/problems/sliding-window-maximum/

import unittest
from pprint import pprint
import random
from collections import deque


def solution_bruteforce(arr, k):
    if k == 1:
        return arr

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
    if k == 1:
        return arr

    d = deque()
    result = []
    arr_enumerated = list(enumerate(arr))  # (i, v)

    for i in range(k):
        put_in_deque(d, arr_enumerated[i])
    result.append(d[-1][1])

    for i in range(k, len(arr_enumerated)):
        if arr_enumerated[i - k] == d[-1]:
            d.pop()

        while d[-1][0] < i - k:
            d.pop()

        put_in_deque(d, arr_enumerated[i])
        result.append(d[-1][1])

    return result


if __name__ == '__main__':
    # arr = [1, 3, -1, -3, 2, 3, 6, 7]

    i = 1
    while True:
        arr = [random.randint(-10000, 10000) for _ in range(1, 222)]
        k = random.randint(1, len(arr) - 1)
        deque_result = solution_deque(arr, k)

        bf_result = solution_bruteforce(arr, k)

        if bf_result != deque_result:
            print("arr = %s" % arr)
            print("k = %s" % k)
            print("expecting = %s" % bf_result)
            print("test = %s" % deque_result)
            if i % 1000 == 0:
                print("ran %s tests" % i)
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

    def test_4(self):
        arr = [3420, 694, 8263, -7263, -5220, 1939, 3365, 141, -9735, -5289, -9038, -805, -2389, -3087, 5317, 3294,
               7546, -9770, 4759, 5882, 9729, -8069, -788, -6206, 1810, -5769, -2980, 715, 7823, -852, -2721, -840,
               -8773, 5411, 4400, -4469, 4653, 1309, -5126, 8191, 7632, -2690, 1388, -4912, -2987, 9991, 9346, -2545,
               -8841, -5873, 7726, -3684, -7902, -7452, -5169, 2285, -7444, -6792, -7941, -9083, 8717, 6856, 6389, 6627,
               8915, -2141, -2783, 4586, -8088, 7028, 2031, -1571, -5643, 8066, -7082, 3617, 2504, -7700, 9443, -9930,
               -3061, -1662, 1356, -332, 513, -9719, 4126, 8317, -116, -4284, -2871, 6705, 3290, -4690, 2366, -8179,
               -3469, 7177, -4776]
        k = 41
        expecting = [9729, 9729, 9729, 9729, 9729, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991,
                     9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991,
                     9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9991, 9443, 9443,
                     9443, 9443, 9443, 9443, 9443, 9443, 9443, 9443, 9443, 9443, 9443]
        self.assertEqual(expecting, solution_deque(arr, k))

    def test_5(self):
        arr = [-4301, -2114, 8926, 6147, -1766, 3947, 669, 3070, 7816, 8942, 7003, 4094, -1792, 3587, -4861, 1009,
               -7014, 4177, 7003, -1257, 1058]
        k = 9
        expecting = [8926, 8942, 8942, 8942, 8942, 8942, 8942, 8942, 8942, 8942, 7003, 7003, 7003]
        self.assertEqual(expecting, solution_deque(arr, k))

# chokes on: [10000 .. -10000], 10007
