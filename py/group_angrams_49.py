#!/usr/bin/env python

# https://leetcode.com/problems/group-anagrams/

import unittest
from pprint import pprint
import random


def solution(wordlist):
    key_to_words = {}
    for w in wordlist:
        key = ''.join(sorted(list(w)))
        if key not in key_to_words:
            key_to_words[key] = []
        key_to_words[key].append(w)

    result = list(key_to_words.values())
    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        pprint(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
