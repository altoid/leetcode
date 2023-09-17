#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(path):
    components = path.split('/')
    components = [c for c in components if c != '']
    components = [c for c in components if c != '.']

    stack = []
    for c in components:
        if c == '..':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(c)
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_5(self):
        path = "/a/b/c/../d/e///"
        expecting = '/a/b/d/e'
        self.assertEqual(expecting, solution(path))

    def test_4(self):
        path = "//..//"
        expecting = '/'
        self.assertEqual(expecting, solution(path))

    def test_3(self):
        path = "//.."
        expecting = '/'
        self.assertEqual(expecting, solution(path))

    def test_2(self):
        path = "/.."
        expecting = '/'
        self.assertEqual(expecting, solution(path))

    def test_1(self):
        path = "/a/b//c/"
        expecting = '/a/b/c'
        self.assertEqual(expecting, solution(path))
