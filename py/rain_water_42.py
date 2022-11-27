#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


# idea
# starting at level 0, traverse the array looking for 0s that are between larger values.
# change all the 0s that are between those larger values to 1.  count the number of blocks we change.

# keep increasing levels.

def next_hole_at_level(arr, level):
    """
    give me the array slice of the next slot we can fill at this level.  return None if no candidates.
    """
    i = 0
    while i < len(arr) and arr[i] <= level:
        i += 1

    if i == len(arr):
        return None

    # arr[i] > level
    while i < len(arr) and arr[i] > level:
        i += 1

    if i == len(arr):
        return None

    # arr[i] == level and is to the right of something taller.

    j = i
    while j < len(arr) and arr[j] <= level:
        j += 1

    if j == len(arr):
        return None

    # are we here?  then there is some element to the left of [i] that is bigger than level, so we have a cistern.
    return i, j


def fill_level(arr, level):
    result = 0

    slice = next_hole_at_level(arr, level)
    while slice is not None:
        i, j = slice
        delta = j - i
        arr = arr[:i] + [level + 1] * delta + arr[j:]
        result += delta
        slice = next_hole_at_level(arr, level)

    return result, arr


def solution(arr):
    if not arr:
        return 0

    total = 0
    minlevel = min(arr)
    maxlevel = max(arr)

    for l in range(minlevel, maxlevel):
        result, arr = fill_level(arr, l)
        if result == 0:
            break
        total += result

    return total


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_2(self):
        arr = [4, 2, 0, 3, 2, 5]
        expecting = 9
        self.assertEqual(expecting, solution(arr))

    def test_1(self):
        arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expecting = 6
        self.assertEqual(expecting, solution(arr))
