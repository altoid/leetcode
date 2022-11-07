#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random
from math import sqrt


def powers_to_value(t):
    return 2 ** t[0] * 3 ** t[1] * 5 ** t[2]


def solution(nth):
    bucket = set()
    val_to_powers = {}

    initial = (0, 0, 0)
    minkey = powers_to_value(initial)
    val_to_powers[minkey] = initial
    bucket.add(initial)

    #

    for k in range(nth):
        minkey = min(val_to_powers.keys())
        powers = val_to_powers[minkey]

        bucket.remove(powers)
        del val_to_powers[minkey]

        x = list(powers)
        successors = [x[:], x[:], x[:]]
        for i in range(len(successors)):
            successors[i][i] += 1

        for s in successors:
            t = tuple(s)
            if t in bucket:
                continue

            v = powers_to_value(t)
            val_to_powers[v] = t
            bucket.add(t)

    return minkey


if __name__ == '__main__':
    # the 1692nd is exactly 2 ** 31!
    print(solution(1692))


class MyTest(unittest.TestCase):
    def test_3(self):
        n = solution(124)
        expecting = 3072
        self.assertEqual(expecting, n)

    def test_2(self):
        n = solution(124)
        expecting = 3072
        self.assertEqual(expecting, n)

    def test_1(self):
        n = solution(10)
        expecting = 12
        self.assertEqual(expecting, n)
