#!/usr/bin/env python

import unittest
from pprint import pprint


class Node:
    def __init__(self, x: int, nxt=None, random=None):
        self.val = int(x)
        self.next = nxt
        self.random = random


def solution(head):
    if not head:
        return None

    id_mappings = {}

    newhead = Node(head.val)
    to_copy = head.next
    dest = newhead
    id_mappings[head] = newhead
    while to_copy is not None:
        new_node = Node(to_copy.val)
        id_mappings[to_copy] = new_node
        dest.next = new_node
        dest = new_node
        to_copy = to_copy.next

    p = head
    np = newhead
    while True:
        if not p:
            break

        if p.random in id_mappings:
            np.random = id_mappings[p.random]

        p = p.next
        np = np.next

    return newhead


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        pass
