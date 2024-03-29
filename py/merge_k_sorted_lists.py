#!/usr/bin/env python

# https://leetcode.com/problems/merge-k-sorted-lists/

# idea:  divide and conquer.  chop the list of lists in half and process each half separately then merge the results.
# the basis case is we have
#
# 0 lists - do nothing
# 1 list - return it without further action
# 2 lists - merge them, this is easy; return the merged list
# more than 2 lists - recur.

import unittest
from pprint import pprint
from llutils import ListNode, ll_to_list, ll_to_string, to_linked_list, reverse

def merge_2(l1, l2):
    p1 = l1
    p1next = p1.next if p1 else None
    p2 = l2
    p2next = p2.next if p2 else None
    head = tail = None

    while p1 or p2:
        if p1 and p2:
            if p1.val < p2.val:
                n = p1
                p1 = p1next
                if p1next:
                    p1next = p1.next
            else:
                n = p2
                p2 = p2next
                if p2next:
                    p2next = p2.next
        elif p1:
            n = p1
            p1 = p1next
            if p1next:
                p1next = p1.next
        else:
            n = p2
            p2 = p2next
            if p2next:
                p2next = p2.next

        n.next = None

        if not head:
            head = tail = n
        else:
            tail.next = n
            tail = n

    return head


def helper(lists, start, end):
    if end - start < 2:
        return lists[start]

    if end == start + 2:
        return merge_2(lists[start], lists[start + 1])

    m = (start + end) // 2
    return merge_2(helper(lists, start, m), helper(lists, m, end))


class Solution:
    def mergeKLists(self, lists):
        if lists:
            return helper(lists, 0, len(lists))
        return None


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
        llresult = merge_2(lla, llb)
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

    def test_merge_6(self):
        lists = []
        self.assertIsNone(self.s.mergeKLists(lists))


    def test_merge_null(self):
        self.assertEqual([], ll_to_list(self.s.mergeKLists([None])))