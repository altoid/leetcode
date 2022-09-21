#!/usr/bin/env python

import unittest
import random
from pprint import pprint


def running_sum(arr):
    """
    given a list of ints arr, return another list b such that b[i] == SUM(arr[0..i])
    """
    total = 0
    result = []
    for a in arr:
        total += a
        result.append(total)

    return result


class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class MonoDeque(object):
    """
    class which maintains the invariant that the values in the deque are monotonically nondecreasing
    left to right.  if we push something on the right end where val(rightmost) > val(item), this will
    remove all of the rightmost items with a greater value than the to-be-inserted item.
    """

    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def __bool__(self):
        return self.count != 0

    def __len__(self):
        return self.count

    def rightmost(self):
        return self.tail.val

    def leftmost(self):
        return self.head.val

    def insert_right(self, item):
        """
        item is (index, value) pair
        """
        n = Node(item)
        if not self.head:
            self.head = n
            self.tail = n
            self.count = 1
        else:
            while self.tail and self.tail.val[1] > n.val[1]:
                nukeme = self.tail
                if nukeme.prev:
                    self.tail = nukeme.prev
                    nukeme.prev = None
                    self.tail.next = None
                else:
                    self.head = self.tail = None
                self.count -= 1

            if self.tail:
                self.tail.next = n
                n.prev = self.tail
                self.tail = n
            else:
                self.head = self.tail = n
            self.count += 1

    def remove_left(self):
        """
        caller must check nonempty
        """
        nukeme = self.head
        if self.head.next:
            self.head = self.head.next
            nukeme.next = None
            self.head.prev = None
        else:
            self.head = self.tail = None

        self.count -= 1

        return nukeme.val

    def __str__(self):
        p = self.head
        substrings = []
        while p:
            substrings.append(str(p.val))
            p = p.next
        result = ', '.join(substrings)
        result = "[" + result + "]"
        return result


def solution(arr, k):
    sums = running_sum(arr)
    indexed_sums = list(enumerate(sums))

    # pairs are (index, item)

    subarray_len = shortest_subarray_len = len(arr) + 1
    md = MonoDeque()
    md.insert_right(indexed_sums[0])
    tally = md.rightmost()[1]
    i = 1

    # special case singleton array because loop assumes len > 1
    if len(arr) == 1:
        tally = arr[0]
        if tally >= k:
            shortest_subarray_len = 1

    while i < len(indexed_sums):

        while tally < k and i < len(indexed_sums):
            md.insert_right(indexed_sums[i])
            tally = md.rightmost()[1]
            i += 1

        if tally >= k:
            subarray_len = len(md)

        leftmost = md.remove_left()
        tally -= leftmost[1]
        while tally >= k and len(md) > 0:
            subarray_len -= 1
            leftmost = md.remove_left()
            tally -= leftmost[1]

        shortest_subarray_len = min(subarray_len, shortest_subarray_len)

    if shortest_subarray_len > len(arr):
        return -1
    return shortest_subarray_len


if __name__ == '__main__':
    arr = [2, 7, 3, -8, 4, 10]
    index_items = list(enumerate(arr))

    d = MonoDeque()
    d.insert_right(index_items[0])
    d.insert_right(index_items[1])
    d.insert_right(index_items[2])
    print(str(d))
    d.insert_right(index_items[3])
    print(str(d))
    d.insert_right(index_items[4])
    d.insert_right(index_items[5])
    print(str(d))


class MyTest(unittest.TestCase):
    def test1(self):
        arr = [2, 7, 3, -8, 4, 10]
        k = 12
        expected = 2
        self.assertEqual(expected, solution(arr, k))

    def test_deque_1(self):
        arr = [2, 7, 3, -8, 4, 10]
        index_items = list(enumerate(arr))

        d = MonoDeque()
        d.insert_right(index_items[0])
        d.insert_right(index_items[1])
        d.insert_right(index_items[2])
        self.assertEqual(2, len(d))
        d.insert_right(index_items[3])
        self.assertEqual(1, len(d))
        d.insert_right(index_items[4])
        d.insert_right(index_items[5])
        self.assertEqual(3, len(d))
        self.assertTrue(bool(d))
        d.remove_left()
        d.remove_left()
        d.remove_left()
        self.assertEqual(0, len(d))
        self.assertFalse(bool(d))

    def test2(self):
        arr = [5]
        k = 4
        expected = 1
        self.assertEqual(expected, solution(arr, k))

    def test3(self):
        arr = [5]
        k = 5
        expected = 1
        self.assertEqual(expected, solution(arr, k))

    def test4(self):
        arr = [5]
        k = 6
        expected = -1
        self.assertEqual(expected, solution(arr, k))

    def test5(self):
        arr = [1, 2]
        k = 4
        expected = -1
        self.assertEqual(expected, solution(arr, k))

    def test6(self):
        arr = [2,-1,2]
        k = 3
        expected = 3
        self.assertEqual(expected, solution(arr, k))
