#!/usr/bin/env python

import unittest
from llutils import to_linked_list, ll_to_list, tail, reverse
from pprint import pprint


# idea - keep 4 pointers:  head and tail of the group we are reversing and one each for the nodes
# immediately before and after the group

def solution(head, k):
    if head is None:
        return head

    if k == 1:
        return head

    newhead = head
    predecessor = None
    head_of_group = head
    tail_of_group = head_of_group
    i = 0
    while i < k - 1:
        if not tail_of_group:
            break
        tail_of_group = tail_of_group.next
        i += 1

    if tail_of_group:
        newhead = tail_of_group

    while tail_of_group:
        successor_of_group = tail_of_group.next
        if predecessor:
            predecessor.next = None
        tail_of_group.next = None

        head_of_group = reverse(head_of_group)
        tail_of_group = tail(head_of_group)

        tail_of_group.next = successor_of_group
        if predecessor:
            predecessor.next = head_of_group

        predecessor = tail_of_group
        head_of_group = predecessor.next

        tail_of_group = head_of_group
        i = 0
        while i < k - 1:
            if not tail_of_group:
                break
            tail_of_group = tail_of_group.next
            i += 1

    return newhead


class MyTest(unittest.TestCase):
    def test1(self):
        l = [1, 2, 3, 4]
        expected = [2, 1, 4, 3]
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test2(self):
        l = [1]
        expected = [1]
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test3(self):
        l = [1, 2, 3, 4, 5]
        expected = [2, 1, 4, 3, 5]
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test4(self):
        l = [1, 2]
        expected = [2, 1]
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test5(self):
        l = []
        expected = []
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test6(self):
        l = [6, 2, 5, 4, 5, 1, 6]
        expected = [2, 6, 4, 5, 1, 5, 6]
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test7(self):
        l = [6, 2, 5]
        expected = [2, 6, 5]
        ll = to_linked_list(l)
        result = solution(ll, 2)
        self.assertEqual(expected, ll_to_list(result))

    def test8(self):
        l = [6, 2, 5, 4, 5, 1, 6]
        expected = [6, 2, 5, 4, 5, 1, 6]
        ll = to_linked_list(l)
        result = solution(ll, 1)
        self.assertEqual(expected, ll_to_list(result))

    def test9(self):
        l = [6, 2, 5, 4, 5, 1, 6]
        expected = [4, 5, 2, 6, 5, 1, 6]
        ll = to_linked_list(l)
        result = solution(ll, 4)
        self.assertEqual(expected, ll_to_list(result))

    def test10(self):
        l = [6, 2, 5, 4, 5, 1, 6]
        expected = [6, 2, 5, 4, 5, 1, 6]
        ll = to_linked_list(l)
        result = solution(ll, 41)
        self.assertEqual(expected, ll_to_list(result))

    def test11(self):
        l = [6, 2, 5, 4, 5, 1, 6]
        expected = [6, 1, 5, 4, 5, 2, 6]
        ll = to_linked_list(l)
        result = solution(ll, 7)
        self.assertEqual(expected, ll_to_list(result))
