#!/usr/bin/env python

# https://leetcode.com/problems/merge-k-sorted-lists/


import unittest
from pprint import pprint


# their definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(l):
    prev = None
    for x in reversed(l):
        n = ListNode(x, prev)
        prev = n
    return prev


def ll_to_string(ll):
    return str(ll_to_list(ll))


def ll_to_list(ll):
    real = []
    n = ll
    while n:
        real.append(n.val)
        n = n.next

    return real


class ListState(object):
    def __init__(self, lst):
        self.ptr = lst
        self.lst = lst

    def valid(self):
        return bool(self.ptr)

    def current_item(self):
        return self.ptr.val

    def increment(self):
        if self.ptr:
            self.ptr = self.ptr.next

    def __str__(self):
        return "{%s - %s}" % (ll_to_string(self.lst), self.ptr.val if self.ptr else "<>")

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
            # pprint(result)
            # pprint(states)
            m = min(valid, key=lambda x: x.current_item())
            # pprint(m)
            result.append(m.current_item())
            m.increment()

            valid = list(filter(lambda x: x.valid(), states))

        # pprint(states)
        # pprint(result)
        return to_linked_list(result)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_ll_1(self):
        lst = [1, 2, 3, 4]
        ll = to_linked_list(lst)
        self.assertEqual("[1, 2, 3, 4]", ll_to_string(ll))

    def test_ll_2(self):
        lst = [1]
        ll = to_linked_list(lst)
        self.assertEqual("[1]", ll_to_string(ll))

    def test_ll_3(self):
        lst = []
        ll = to_linked_list(lst)
        self.assertEqual("[]", ll_to_string(ll))

    def test_list_state_1(self):
        l = to_linked_list([1])
        ls = ListState(l)
        self.assertTrue(ls.valid())
        ls.increment()
        self.assertFalse(ls.valid())

    def test_list_state_2(self):
        l = to_linked_list([])
        ls = ListState(l)
        self.assertFalse(ls.valid())

    def test_list_state_3(self):
        l = to_linked_list([1, 2])
        ls = ListState(l)
        self.assertTrue(ls.valid())
        self.assertEqual(1, ls.current_item())
        ls.increment()
        self.assertEqual(2, ls.current_item())
        self.assertTrue(ls.valid())

    def test_merge_1(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

        lists = map(lambda x: to_linked_list(x), lists)
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], ll_to_list(self.s.mergeKLists(lists)))

    def test_merge_2(self):
        lists = [[]]

        self.assertEqual([], ll_to_list(self.s.mergeKLists(lists)))
