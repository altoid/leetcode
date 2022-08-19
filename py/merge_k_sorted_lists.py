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


def reverse(ll):
    """
    reverse the linked list; this modifies the list by changing all the pointers.
    """

    p0 = None
    p1 = ll
    p2 = ll.next if ll else None

    while p2:
        p1.next = p0
        p0 = p1
        p1 = p2
        p2 = p2.next
    if p1:
        p1.next = p0
    return p1


class Solution:
    def merge_2(self, l1, l2):
        p1 = l1
        p2 = l2
        prev = None
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    n = ListNode(p1.val, prev)
                    p1 = p1.next
                else:
                    n = ListNode(p2.val, prev)
                    p2 = p2.next
            elif p1:
                n = ListNode(p1.val, prev)
                p1 = p1.next
            else:
                n = ListNode(p2.val, prev)
                p2 = p2.next
            prev = n

        return reverse(prev)

    def helper(self, lists, start, end):
        if end - start < 2:
            return lists[start]

        if end == start + 2:
            return self.merge_2(lists[start], lists[start + 1])

        m = (start + end) // 2
        return self.merge_2(self.helper(lists, start, m), self.helper(lists, m, end))

    def mergeKLists(self, lists):
        return self.helper(lists, 0, len(lists))


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_reverse_1(self):
        ll = to_linked_list([1, 2, 3, 4, 5])
        r = reverse(ll)
        self.assertEqual([5, 4, 3, 2, 1], ll_to_list(r))

    def test_reverse_2(self):
        ll = to_linked_list([1])
        r = reverse(ll)
        self.assertEqual([1], ll_to_list(r))

    def test_reverse_3(self):
        ll = to_linked_list([1, 2])
        r = reverse(ll)
        self.assertEqual([2, 1], ll_to_list(r))

    def test_reverse_4(self):
        ll = to_linked_list([])
        r = reverse(ll)
        self.assertEqual([], ll_to_list(r))

    def merge(self, a, b):
        lla = to_linked_list(a)
        llb = to_linked_list(b)
        llresult = self.s.merge_2(lla, llb)
        control = sorted(a + b)
        test = ll_to_list(llresult)
        self.assertEqual(control, test)

    def test_merge_2_1(self):
        self.merge([1, 2, 3], [4, 5, 6])
        self.merge([1], [4, 5, 6])
        self.merge([1, 2, 3], [4])
        self.merge([1], [4])
        self.merge([], [4, 5, 6])
        self.merge([1, 2, 3], [])
        self.merge([], [])

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

    def test_merge_1(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        lists = list(map(lambda x: to_linked_list(x), lists))

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], ll_to_list(self.s.mergeKLists(lists)))

    def test_merge_2(self):
        lists = [[]]
        lists = list(map(lambda x: to_linked_list(x), lists))

        self.assertEqual([], ll_to_list(self.s.mergeKLists(lists)))

    def test_merge_3(self):
        lists = [[], []]
        lists = list(map(lambda x: to_linked_list(x), lists))

        self.assertEqual([], ll_to_list(self.s.mergeKLists(lists)))

    def test_merge_4(self):
        lists = [[1], []]
        lists = list(map(lambda x: to_linked_list(x), lists))

        self.assertEqual([1], ll_to_list(self.s.mergeKLists(lists)))

    def test_merge_5(self):
        lists = [[1], [7], [2], [9], [5], [1], [1], [2]]
        lists = list(map(lambda x: to_linked_list(x), lists))

        self.assertEqual([1, 1, 1, 2, 2, 5, 7, 9], ll_to_list(self.s.mergeKLists(lists)))

    def test_merge_null(self):
        self.assertEqual([], ll_to_list(self.s.mergeKLists([None])))