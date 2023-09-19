#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(n):
    answer = ''

    q, n = divmod(n, 1000)
    answer += 'M' * q

    if n >= 900:
        answer += 'CM'
        n = n - 900
    elif n >= 500:
        answer += 'D'
        n = n - 500
        q, n = divmod(n, 100)
        answer += 'C' * q
    elif n >= 400:
        answer += 'CD'
        n = n - 400
    elif n >= 100:
        q, n = divmod(n, 100)
        answer += 'C' * q

    if n >= 90:
        answer += 'XC'
        n = n - 90
    elif n >= 50:
        answer += 'L'
        n = n - 50
        q, n = divmod(n, 10)
        answer += 'X' * q
    elif n >= 40:
        answer += 'XL'
        n = n - 40
    elif n >= 10:
        q, n = divmod(n, 10)
        answer += 'X' * q

    if n >= 9:
        answer += 'IX'
        n = n - 9
    elif n >= 5:
        answer += 'V'
        n = n - 5
        answer += 'I' * q
    elif n == 4:
        answer += 'IV'
    else:
        answer += 'I' * n

    return answer


if __name__ == '__main__':
    n = random.randint(1, 3999)
    r = solution(n)
    print(n, r)


class MyTest(unittest.TestCase):
    def test_1(self):
        n = 245
        expecting = 'CCXLV'
        self.assertEqual(expecting, solution(n))
