#!/usr/bin/env python

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


def solution(l1, l2):
    carry = 0
    result = []

    i = 0
    while True:
        if i >= len(l1) and i >= len(l2):
            break

        digit = 0
        if i < len(l1):
            digit += l1[i]
        if i < len(l2):
            digit += l2[i]
        digit += carry
        if digit > 9:
            digit = digit - 10
            carry = 1
        else:
            carry = 0

        result.append(digit)

        i += 1

    if carry:
        result.append(carry)

    return result


class MyTest(unittest.TestCase):
    def test1(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        expecting = [7, 0, 8]
        self.assertEqual(expecting, solution(l1, l2))

    def test2(self):
        l1 = [9, 9, 9, 9, 9, 9, 9]
        l2 = [9, 9, 9, 9]
        expecting = [8, 9, 9, 9, 0, 0, 0, 1]
        self.assertEqual(expecting, solution(l1, l2))
