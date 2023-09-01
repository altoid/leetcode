#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def left_justify(words, width):
    # assume that all the words will fit; pad on the right if needed.
    line = ' '.join(words)
    padding = ' ' * (width - len(line))
    return line + padding

def solution():
    pass


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        words = ['what', 'hath', 'god', 'wrought']
        expecting = 'what hath god wrought'
        result = left_justify(words, 21)
        self.assertEqual(expecting, result)

    def test_2(self):
        words = ['what', 'hath', 'god', 'wrought']
        expecting = 'what hath god wrought   '
        result = left_justify(words, 24)
        self.assertEqual(expecting, result)
