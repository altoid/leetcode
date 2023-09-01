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


def next_line(pos, text, width):
    i = pos + 1
    line = [text[pos]]
    linewidth = len(text[pos])
    while True:
        if i >= len(text):
            return line, None

        if linewidth + 1 + len(text[i]) > width:
            return line, i

        line.append(text[i])
        linewidth += 1 + len(text[i])

        i += 1


def split_text(text, width):
    result = []
    pos = 0
    line, pos = next_line(pos, text, width)
    while pos is not None:
        result.append(line)
        line, pos = next_line(pos, text, width)
    result.append(line)

    return result


def solution(words, width):
    lines = split_text(words, width)
    result = []
    for i in range(len(lines) - 1):
        jline = full_justify(lines[i], width)
        result.append(jline)
    jline = left_justify(lines[-1], width)
    result.append(jline)

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_13(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        width = 16
        expecting = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        result = solution(words, width)
        self.assertEqual(expecting, result)

    def test_12(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        width = 16
        expecting = [
            ["This", "is", "an"],
            ["example", "of", "text"],
            ["justification."]
        ]
        result = split_text(words, width)
        self.assertEqual(expecting, result)

    def test_11(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        width = 16
        expecting = ["justification."]
        line, pos = next_line(6, words, width)
        self.assertIsNone(pos)
        self.assertEqual(expecting, line)

    def test_10(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        width = 16
        expecting = ["example", "of", "text"]
        line, pos = next_line(3, words, width)
        self.assertEqual(6, pos)
        self.assertEqual(expecting, line)

    def test_9(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        width = 16
        expecting = ["This", "is", "an"]
        line, pos = next_line(0, words, width)
        self.assertEqual(3, pos)
        self.assertEqual(expecting, line)

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

