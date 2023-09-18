#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(prices):
    if len(prices) < 2:
        return 0

    # keep track of all increasing windows
    left = right = 0
    totalprofit = 0
    current_window_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[right]:
            current_window_profit += (prices[i] - prices[right])
            right = i
        elif prices[i] < prices[right]:
            left = right = i
            totalprofit += current_window_profit
            current_window_profit = 0

    totalprofit += current_window_profit

    return totalprofit


def generate_array():
    length = random.randint(1, 10)
    return [random.randint(1, 40) for _ in range(length)]


if __name__ == '__main__':
    arr = generate_array()
    answer = solution(arr)
    print(arr)
    print(answer)


class MyTest(unittest.TestCase):
    def test_4(self):
        arr = [37, 10, 7, 13, 21]
        expected = 14
        self.assertEqual(expected, solution(arr))

    def test_3(self):
        arr = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, solution(arr))

    def test_2(self):
        arr = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(expected, solution(arr))

    def test_1(self):
        arr = [7, 1, 5, 3, 6, 4]
        expected = 7
        self.assertEqual(expected, solution(arr))
