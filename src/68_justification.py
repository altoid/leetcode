#!/usr/bin/env python

import unittest
from pprint import pprint


def min_length(words):
    """
    :param words: a list of words
    :return: the minimum length of a line of text with these words in them.
    """

    if not words:
        return 0

    l = sum(map(len, words))
    l += len(words) - 1
    return l


def justify_line(line, maxlength):
    # if the line just has one word, right-pad and be done with it.
    nchars = sum(map(len, line))
    spaces_needed = maxlength - nchars
    if len(line) == 1:
        return line[0] + " " * spaces_needed

    inter_space = spaces_needed / (len(line) - 1)
    extras = spaces_needed % (len(line) - 1)
    result = ""
    for w in line[:-1]:
        result += w
        result += " " * inter_space
        if extras > 0:
            result += " "
            extras -= 1
    result += line[-1]
    return result


def justify(words, maxlength):
    """
    A word is defined as a character sequence consisting of non-space characters only.

    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.

    The input array words contains at least one word.

    :param words:
    :param maxlength:
    :return:
    """

    # first, compile the array of words into a list of lines.  this will be an array of arrays.

    current_line = [words[0]]
    text = []
    for w in words[1:]:
        if min_length(current_line) + 1 + len(w) > maxlength:
            text.append(current_line)
            current_line = []

        current_line.append(w)

    text.append(current_line)

    result = [justify_line(x, maxlength) for x in text]
    return result


class MyTest(unittest.TestCase):
    def test_min_length(self):
        self.assertEqual(12, min_length(['theomorphism']))
        self.assertEqual(13, min_length(['i', 'like', 'cheese']))
        self.assertEqual(0, min_length([]))

    def test_justify_line(self):
        self.assertEqual("Science  is  what we", justify_line(["Science", "is", "what", "we"], 20))

    def test_single_word(self):
        words = ['food']
        maxwidth = 11

        text = justify(words, maxwidth)
        pprint(text)

    def test_example_3(self):
        words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                 "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
        maxWidth = 20

        text = justify(words, maxWidth)
        pprint(text)
