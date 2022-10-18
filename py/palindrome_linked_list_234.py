#!/usr/bin/env python3

import unittest


# https://leetcode.com/problems/palindrome-linked-list/

# solution that uses O(1) space.
#
# idea:  find the middle of the list.  reverse the rest.
# traverse both, comparing pairwise.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def create_list(arr):
    head = None
    for x in reversed(arr):
        n = Node(x)
        n.next = head
        head = n
    return head


def print_list(head):
    p = head
    lst = []
    while p:
        lst.append(p.value)
        p = p.__next__

    slst = list(map(str, lst))
    print("<%s>" % ", ".join(slst))


def length(lst):
    # get the length of the list
    l = 0
    p = lst
    while p:
        l += 1
        p = p.__next__

    return l


def find_middle(lst):
    """
    for even-length return the node at position n/2.
    for odd-length lists, n/2 + 1.  this will be the
    node right in the middle.
    """
    l = length(lst)
    stophere = (l + 1) // 2

    p = lst
    for c in range(stophere - 1):
        p = p.__next__

    return p


def is_palindrome(lst):
    m = find_middle(lst)
    rest = m.__next__
    m.next = None

    prev = None
    curr = rest
    next = None

    while curr:
        next = curr.__next__
        curr.next = prev
        prev = curr
        curr = next

    rest = prev

    # rest is never longer than lst
    plst = lst
    prest = rest
    while prest:
        if plst.value != prest.value:
            return False
        plst = plst.__next__
        prest = prest.__next__

    return True


class MyTest(unittest.TestCase):
    def test_length(self):
        lst = create_list([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(8, length(lst))
        lst = create_list([1])
        self.assertEqual(1, length(lst))
        lst = create_list([])
        self.assertEqual(0, length(lst))

    def test_find_middle_even(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        lst = create_list(arr)
        n = find_middle(lst)
        self.assertEqual(4, n.value)

    def test_find_middle_odd(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        lst = create_list(arr)
        n = find_middle(lst)
        self.assertEqual(4, n.value)

    def test_is_palindrome_even_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        lst = create_list(arr)
        self.assertFalse(is_palindrome(lst))

    def test_is_palindrome_odd_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        lst = create_list(arr)
        self.assertFalse(is_palindrome(lst))

    def test_is_palindrome_even_2(self):
        arr = [1, 2, 3, 4, 4, 3, 2, 1]
        lst = create_list(arr)
        self.assertTrue(is_palindrome(lst))

    def test_is_palindrome_odd_2(self):
        arr = [1, 2, 3, 4, 3, 2, 1]
        lst = create_list(arr)
        self.assertTrue(is_palindrome(lst))
