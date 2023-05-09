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

    def point_to_next_run(self):
        """
        set the pointer to the beginning of the next nontrivial run.  sets still_mo to False if doing so runs off
        the end of the encoding.  returns the number of places the pointer was moved, or -1 if we couldn't move it.
        """
        advance = self.encoding[self.current_run] - self.position_in_current_run + 1
        self.current_run += 2
        while self.current_run < len(self.encoding) and self.encoding[self.current_run] == 0:
            self.current_run += 2

        if self.current_run >= len(self.encoding):
            self.still_mo = False
            return -1

        self.position_in_current_run = 1

        return advance

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

        # advance the pointer to the beginning of the next run.
        advance = self.point_to_next_run()
        if advance < 0:
            return -1

        n -= advance

        while self.still_mo and n - self.encoding[self.current_run] > 0:
            n -= self.encoding[self.current_run]
            self.current_run += 2
            if self.current_run >= len(self.encoding):
                self.still_mo = False

        if not self.still_mo:
            return -1

        self.position_in_current_run += n
        return self.encoding[self.current_run + 1]


def solution():
    pass


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        encoding = [3, 'a', 3, 'b', 0, '#', 3, 'c']
        obj = RLEIterator(encoding)
        result = obj.next(2)
        while result != -1:
            print(result)
            result = obj.next(2)

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

    def test_4(self):
        encoding = [1, 'a', 0, '!', 0, '@', 0, '+', 1, 'b']
        obj = RLEIterator(encoding)
        result = obj.next(1)
        while result != -1:
            print(result)
            result = obj.next(1)
