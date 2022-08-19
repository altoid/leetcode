#!/usr/bin/env python

# https://leetcode.com/problems/merge-k-sorted-lists/


import unittest
from pprint import pprint


class ListState(object):
    def __init__(self, lst):
        self.ptr = 0
        self.lst = lst

    def valid(self):
        return self.ptr < len(self.lst)

    def current_item(self):
        return self.lst[self.ptr]

    def increment(self):
        self.ptr += 1

    def __str__(self):
        return "{%s - %s}" % (str(self.lst), self.ptr)

    def __repr__(self):
        return str(self)


class Solution:
    def mergeKLists(self, lists):
        states = [ListState(l) for l in lists]

        result = []
        # get all the valid status
        valid = list(filter(lambda x: x.valid(), states))

        # return the min value among the valid lists
        while len(valid) > 0:
            pprint(result)
            pprint(states)
            m = min(valid, key=lambda x: x.current_item())
            pprint(m)
            result.append(m.current_item())
            m.increment()

            valid = list(filter(lambda x: x.valid(), states))

        pprint(states)
        pprint(result)
        return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_list_state_1(self):
        l = [1]
        ls = ListState(l)
        self.assertTrue(ls.valid())
        ls.increment()
        self.assertFalse(ls.valid())

    def test_list_state_2(self):
        l = []
        ls = ListState(l)
        self.assertFalse(ls.valid())

    def test_list_state_3(self):
        l = [1, 2]
        ls = ListState(l)
        self.assertTrue(ls.valid())
        self.assertEqual(l[0], ls.current_item())
        ls.increment()
        self.assertEqual(l[1], ls.current_item())
        self.assertTrue(ls.valid())

    def test_merge_1(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], self.s.mergeKLists(lists))

    def test_merge_2(self):
        lists = [[]]

        self.assertEqual([], self.s.mergeKLists(lists))
