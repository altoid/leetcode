#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(prices):
    if len(prices) < 2:
        return 0

    left = right = 0
    maxprice = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[right]:
            right = i
            maxprice = max(maxprice, prices[right] - prices[left])
        elif prices[i] < prices[left]:
            left = right = i

    return maxprice


def generate_array():
    length = random.randint(1, 10)
    return [random.randint(1, 40) for _ in range(length)]


if __name__ == '__main__':
    arr = generate_array()
    answer = solution(arr)
    print(arr)
    print(answer)


class MyTest(unittest.TestCase):
    def test_2(self):
        arr = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, solution(arr))

    def test_1(self):
        arr = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(expected, solution(arr))
