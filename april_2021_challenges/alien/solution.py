#!/usr/bin/env python

# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3702/

import unittest
from pprint import pprint


def mycmp(a, b, letters_to_pos):
    a_pos = [letters_to_pos[x] for x in list(a)]
    b_pos = [letters_to_pos[x] for x in list(b)]

    min_length = min(len(a), len(b))
    for i in xrange(min_length):
        if a_pos[i] < b_pos[i]:
            return -1
        if a_pos[i] > b_pos[i]:
            return 1

    return len(a) - len(b)


def is_sorted(words, alphabet):
    """

    :param words:
    :param alphabet:  a permutation of the 26 lowercase letters
    :return:
    """
    if not words:
        return True

    if len(words) == 1:
        return True

    # turn the alphabet into a dict that maps the letters to their position in the alphabet.
    letters_to_pos = dict(zip(alphabet, [x for x in xrange(len(alphabet))]))

    for i in xrange(len(words) - 1):
        if mycmp(words[i], words[i + 1], letters_to_pos) > 0:
            return False
    return True


class MyTest(unittest.TestCase):
    def test_cmp_1(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letters_to_pos = dict(zip(alphabet, [x for x in xrange(len(alphabet))]))

        self.assertTrue(mycmp('a', 'b', letters_to_pos) < 0)
        self.assertTrue(mycmp('b', 'a', letters_to_pos) > 0)
        self.assertTrue(mycmp('a', 'a', letters_to_pos) == 0)
        self.assertTrue(mycmp('a', 'aaaaaa', letters_to_pos) < 0)
        self.assertTrue(mycmp('aaaaaaaaa', 'b', letters_to_pos) < 0)

    def test_cmp_2(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'[::-1]
        letters_to_pos = dict(zip(alphabet, [x for x in xrange(len(alphabet))]))

        self.assertTrue(mycmp('a', 'b', letters_to_pos) > 0)
        self.assertTrue(mycmp('b', 'a', letters_to_pos) < 0)
        self.assertTrue(mycmp('a', 'a', letters_to_pos) == 0)
        self.assertTrue(mycmp('a', 'aaaaaa', letters_to_pos) < 0)
        self.assertTrue(mycmp('aaaaaaaaa', 'b', letters_to_pos) > 0)

    def test1(self):
        words = ['hello', 'leetcode']
        alphabet = 'hlabcdefgijkmnopqrstuvwxyz'
        print is_sorted(words, alphabet)

    def test2(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'[::-1]
        words = ['hello', 'leetcode']
        self.assertFalse(is_sorted(words, alphabet))
