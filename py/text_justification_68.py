#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def left_justify(words, width):
    # assume that all the words will fit; pad on the right if needed.
    line = ' '.join(words)
    padding = ' ' * (width - len(line))
    return line + padding


def full_justify(words, width):
    if len(words) == 1:
        return left_justify(words, width)

    min_width = sum(map(len, words))
    spaces_needed = width - min_width

    q, r = divmod(spaces_needed, len(words) - 1)
    padding = []
    for i in range(r):
        padding.append(q + 1)
    for i in range(len(words) - 1 - r):
        padding.append(q)

    line = ''
    for i in range(len(words) - 1):
        line += words[i]
        line += ' ' * padding[i]
    line += words[-1]
    return line


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

    def test_3(self):
        word = 'tintinnabulation'
        words = [word]
        expecting = word
        result = left_justify(words, len(word))
        self.assertEqual(expecting, result)

    def test_4(self):
        word = 'tintinnabulation'
        padding = 5
        words = [word]
        expecting = word + ' ' * padding
        result = left_justify(words, len(word) + padding)
        self.assertEqual(expecting, result)

    def test_5(self):
        words = ['what', 'hath', 'god', 'wrought']
        expecting = 'what hath god wrought'
        result = full_justify(words, 21)
        self.assertEqual(expecting, result)

    def test_6(self):
        words = ['what', 'hath', 'god', 'wrought']
        expecting = 'what  hath god wrought'
        result = full_justify(words, 22)
        self.assertEqual(expecting, result)

    def test_7(self):
        word = 'tintinnabulation'
        words = [word]
        expecting = word
        result = full_justify(words, len(word))
        self.assertEqual(expecting, result)

    def test_8(self):
        word = 'tintinnabulation'
        padding = 5
        words = [word]
        expecting = word + ' ' * padding
        result = full_justify(words, len(word) + padding)
        self.assertEqual(expecting, result)

