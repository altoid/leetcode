#!/usr/bin/env python

import unittest
import llutils
from pprint import pprint


def solution(ll):
    if ll is None:
        return ll

    if ll.next is None:
        return ll

    # list has at least 2 items

    p0 = None
    p1 = ll
    p2 = ll.next
    head = p2
    p3 = p2.next

    while p2:
        if p0:
            p0.next = p2
        p1.next = p3
        p2.next = p1

        p0 = p1
        p1 = p2 = p3 = None
        if p0:
            p1 = p0.next
        if p1:
            p2 = p1.next
        if p2:
            p3 = p2.next

    return head


class MyTest(unittest.TestCase):
    def test1(self):
        l = [1, 2, 3, 4]
        expected = [2, 1, 4, 3]
        ll = llutils.to_linked_list(l)
        result = solution(ll)
        self.assertEqual(expected, llutils.ll_to_list(result))

    def test2(self):
        l = [1]
        expected = [1]
        ll = llutils.to_linked_list(l)
        result = solution(ll)
        self.assertEqual(expected, llutils.ll_to_list(result))

    def test3(self):
        l = [1, 2, 3, 4, 5]
        expected = [2, 1, 4, 3, 5]
        ll = llutils.to_linked_list(l)
        result = solution(ll)
        self.assertEqual(expected, llutils.ll_to_list(result))

    def test4(self):
        l = [1, 2]
        expected = [2, 1]
        ll = llutils.to_linked_list(l)
        result = solution(ll)
        self.assertEqual(expected, llutils.ll_to_list(result))

    def test5(self):
        l = []
        expected = []
        ll = llutils.to_linked_list(l)
        result = solution(ll)
        self.assertEqual(expected, llutils.ll_to_list(result))

    def test6(self):
        l = [6, 2, 5, 4, 5, 1, 6]
        expected = [2, 6, 4, 5, 1, 5, 6]
        ll = llutils.to_linked_list(l)
        result = solution(ll)
        self.assertEqual(expected, llutils.ll_to_list(result))
