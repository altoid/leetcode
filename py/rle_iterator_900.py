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
        self.still_mo = bool(self.encoding)

    def next(self, n):

        # cases:
        #
        # 1.  incrementing the pointer keeps us in the current run
        # 2.  or puts us into a new run
        # 2a. possibly skipping 1 or more whole runs along the way
        # 3.  incrementing the pointer runs us off the end of the whole encoding
        #     and we have to return -1 for this and future next() invocations.

        # degenerate cases:
        if not self.still_mo:
            return -1

        # case 1:
        if self.position_in_current_run + n <= self.encoding[self.current_run]:
            self.position_in_current_run += n
            return self.encoding[self.current_run + 1]

        # case 2:
        while self.still_mo and n - self.encoding[self.current_run] > 0:
            n -= self.encoding[self.current_run]
            self.current_run += 2
            if self.current_run >= len(self.encoding):
                self.still_mo = False

        if not self.still_mo:
            return -1

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

    def test_3(self):
        encoding = [1, 'a', 5, 'b', 0, '#', 4, 'c']
        obj = RLEIterator(encoding)
        result = obj.next(10)
        while result != -1:
            print(result)
            result = obj.next(10)
