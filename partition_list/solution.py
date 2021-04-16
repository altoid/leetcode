#!/usr/bin/env python

# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3707/

import unittest


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
        p = p.next

    slst = map(str, lst)
    print "<%s>" % ", ".join(slst)


def partition_list(head, k):
    l_head = l_tail = ge_head = ge_tail = None
    p = head
    tail_changed = None
    while p:
        if p.value < k:
            if l_tail:
                l_tail.next = p
            l_tail = p
            tail_changed = l_tail
            if not l_head:
                l_head = p
        else:
            if ge_tail:
                ge_tail.next = p
            ge_tail = p
            tail_changed = ge_tail
            if not ge_head:
                ge_head = p

        p = p.next

        if tail_changed:
            tail_changed.next = None

    if l_tail:
        l_tail.next = ge_head
        return l_head

    return ge_head


if __name__ == '__main__':
    arr = [1, 4, 3, 2, 5, 2]
    l = create_list(arr)
    print_list(l)
    l = partition_list(l, 3)
    print_list(l)


class MyTest(unittest.TestCase):

    # empty list
    def test0(self):
        arr = []
        l = create_list(arr)
        l = partition_list(l, 3)
        print_list(l)

    # - list where key is not present
    def test1(self):
        arr = [1, 4, 3, 2, 5, 2]
        l = create_list(arr)
        l = partition_list(l, 3)
        print_list(l)

    # - list consisting of only the key
    def test2(self):
        arr = [3, 3, 3, 3, 3]
        l = create_list(arr)
        l = partition_list(l, 3)
        print_list(l)

    # - singleton list
    def test_singleton_1(self):
        arr = [1]
        l = create_list(arr)
        l = partition_list(l, 3)
        print_list(l)

    def test_singleton_2(self):
        arr = [3]
        l = create_list(arr)
        l = partition_list(l, 3)
        print_list(l)

    def test_singleton_3(self):
        arr = [6]
        l = create_list(arr)
        l = partition_list(l, 3)
        print_list(l)

    # - list consisting of only < the key
    def test3(self):
        arr = [1, 4, 3, 2, 5, 2]
        l = create_list(arr)
        l = partition_list(l, 33)
        print_list(l)

    # - list consisting of >= the key
    def test4(self):
        arr = [1, 4, 3, 2, 5, 2]
        l = create_list(arr)
        l = partition_list(l, 1)
        print_list(l)

    # - list consisting of > the key
    def test5(self):
        arr = [1, 4, 3, 2, 5, 2]
        l = create_list(arr)
        l = partition_list(l, 0)
        print_list(l)

    def test6(self):
        arr = [22, 33, 44, 55, 66, 77, 88, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        l = create_list(arr)
        l = partition_list(l, 10)
        print_list(l)
