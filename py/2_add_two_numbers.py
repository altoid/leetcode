#!/usr/bin/env python

import unittest
from pprint import pprint
from llutils import ListNode, to_linked_list, ll_to_list


def solution(l1, l2):
    carry = 0
    head = tail = None
    p1 = l1
    p2 = l2

    while True:
        if not p1 and not p2:
            break

        digit = 0
        if p1:
            digit += p1.val
        if p2:
            digit += p2.val
        digit += carry
        if digit > 9:
            digit = digit - 10
            carry = 1
        else:
            carry = 0

        node = ListNode(digit)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next

        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    if carry:
        node = ListNode(carry)
        tail.next = node

    return head


class MyTest(unittest.TestCase):
    def test1(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        expecting = [7, 0, 8]
        ll1 = to_linked_list(l1)
        ll2 = to_linked_list(l2)
        result = solution(ll1, ll2)
        self.assertEqual(expecting, ll_to_list(result))

    def test2(self):
        l1 = [9, 9, 9, 9, 9, 9, 9]
        l2 = [9, 9, 9, 9]
        expecting = [8, 9, 9, 9, 0, 0, 0, 1]
        ll1 = to_linked_list(l1)
        ll2 = to_linked_list(l2)
        result = solution(ll1, ll2)
        self.assertEqual(expecting, ll_to_list(result))
