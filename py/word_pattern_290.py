#!/usr/bin/env python

import unittest
from pprint import pprint
import random


def solution(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False

    zipped = zip(list(pattern), words)

    letter_to_word = {}
    word_to_letter = {}

    for t in zipped:
        letter, word = t
        if letter not in letter_to_word:
            letter_to_word[letter] = word
        elif letter_to_word[letter] != word:
            return False

        if word not in word_to_letter:
            word_to_letter[word] = letter
        elif word_to_letter[word] != letter:
            return False

    return True


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        self.assertTrue(solution(pattern, s))

    def test_2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        self.assertFalse(solution(pattern, s))

    def test_3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        self.assertFalse(solution(pattern, s))

    def test_4(self):
        pattern = "abba"
        s = "dog cat cat"
        self.assertFalse(solution(pattern, s))

    def test_5(self):
        pattern = "abba"
        s = "dog dog dog dog"
        self.assertFalse(solution(pattern, s))

