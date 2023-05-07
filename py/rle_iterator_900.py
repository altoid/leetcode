#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


class RLEIterator(object):
    def __init__(self, encoding):
        self.encoding = encoding
        self.current_run = 0
        self.position_in_current_run = 0  # positions start from 1
        self.no_mo = False

    def next(self, n):
        if self.current_run >= len(self.encoding):
            return -1

        if self.no_mo:
            return -1

        # deal with n == 0 later

        run_remaining = self.encoding[self.current_run] - self.position_in_current_run

        advance = min(run_remaining, n)

        if n > run_remaining:
            n -= run_remaining
            self.current_run += 2
            if self.current_run >= len(self.encoding):
                self.no_mo = True
                return -1

            while n - self.encoding[self.current_run] >= 0:
                n -= self.encoding[self.current_run]
                self.current_run += 2
        else:
            # we're staying in this run and not advancing self.current_run

            pass

        self.position_in_current_run = n
        return self.encoding[self.current_run + 1]


def solution():
    pass


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        encoding = [3, 'a', 3, 'b', 0, '#', 3, 'c']
        obj = RLEIterator(encoding)
        result = obj.next(4)
        while result != -1:
            print(result)
            result = obj.next(4)

        # a a a b b b c c c
        #       ^       ^       ^

    def test_2(self):
        encoding = [1, 'a', 1, 'b', 1, 'c']
        obj = RLEIterator(encoding)
        result = obj.next(1)
        while result != -1:
            print(result)
            result = obj.next(1)
