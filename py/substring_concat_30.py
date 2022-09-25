#!/usr/bin/env python

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# notes
#
# - assume that no member of <words> is contained in any other word
# - <words> can contain duplicates; each duplicate must be present in the substring
# - it may be that some or none of the words is present in the text

import unittest
from pprint import pprint
import random
import re


def visit(positions_to_words, word_counts, all_indices, fromhere, nwords):
    """
    fromhere is an index into all_indices
    """

    ledger = {}
    for w in word_counts.keys():
        ledger[w] = 0

    if len(all_indices) - fromhere < nwords:
        return None

    i = 0
    while i < nwords - 1:
        # the word at fromhere + i is not adjacent to the word at fromhere + i + 1
        w = positions_to_words[all_indices[fromhere + i]]
        if all_indices[fromhere + i + 1] - all_indices[fromhere + i] != len(w):
            # TODO find an optimization where we don't have to keep calling len()
            return None

        ledger[w] += 1
        if ledger[w] > word_counts[w]:
            return None

        i += 1

    w = positions_to_words[all_indices[fromhere + i]]
    ledger[w] += 1
    if ledger[w] > word_counts[w]:
        return None

    for k in word_counts.keys():
        if word_counts[k] != ledger[k]:
            return None

    return all_indices[fromhere]


def solution(text, words):
    # count the number of times each word is to appear in a correct substring
    word_counts = {}
    for w in words:
        if w not in word_counts:
            word_counts[w] = 0
        word_counts[w] += 1

    # get the index of each word as it appears in the text.  create a list of all indexes,
    # an a mapping of indexes to words.

    # create a list of unique words; shake out dups.
    unique_words = list(set(words))
    all_indices = []
    positions_to_words = {}

    pattern = "|".join(unique_words)
    pattern = "(?=(%s))" % pattern
    matches = re.finditer(pattern, text)
    for m in matches:
        span = m.start(1), m.end(1)
        substring = text[span[0]:span[1]]
        positions_to_words[span[0]] = substring
        all_indices.append(span[0])

    # maybe we don't need to do this
    sorted(all_indices)

    result = []
    for i in range(len(all_indices) - len(words) + 1):
        r = visit(positions_to_words, word_counts, all_indices, i, len(words))
        if r is not None:
            result.append(r)

    return result


def futz(s, pattern):
    # if the pattern is a lookahead pattern, spans will be 0-width, i guess because they match 0 chars.
    # if NOT a lookahead pattern, spans are nonzero width.
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.groups())
        print(m.groups()[0])
        print(m.start(1), m.end(1))
        #print(m.span())
        print(m)

    # matches = re.findall(pattern, s)
    # pprint(matches)


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaa"
    pattern = r'(?=(aa))'

    #futz("aaaaaaaaaaaaaa", r'(?=(aa))')
    futz("aaaaabbbbb", r'(?=(aa|bb))')
    #futz("aaaaabbbbb", r'(aa|bb)')

    # result = solution(s, words)
    # pprint(result)

    # s = '1' * 15
    # result = re.findall(r'(?=(11111))', s)
    #
    # pprint(result)
    # for i in result:
    #     print(i.start(1), i.end(1))


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expecting = {6, 9, 12}
        result = set(solution(s, words))
        self.assertEqual(expecting, result)

    def test_2(self):
        s = "barfoofoobarthefoobarman"
        words = ["mairzy", "doates", "pickle"]
        result = solution(s, words)
        expecting = []
        self.assertEqual(expecting, result)

    def test_3(self):
        s = "barfoofooxbarxthefoobarman"
        words = ["bar", "foo", "the"]
        expecting = {14}
        result = set(solution(s, words))
        self.assertEqual(expecting, result)

    def test_4(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the", "foo"]
        expecting = {3, 6}
        result = set(solution(s, words))
        self.assertEqual(expecting, result)

    def test_5(self):
        s = "barfoothefoobarman"
        words = ["bar", "foo"]
        expecting = {9, 0}
        result = set(solution(s, words))
        self.assertEqual(expecting, result)

    def test_6(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expecting = []
        result = solution(s, words)
        self.assertEqual(expecting, result)

    def test_7(self):
        s = "aaaaaaaaaaaaaa"  # len == 14
        words = ["aa", "aa"]
        expecting = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        result = set(solution(s, words))
        self.assertEqual(expecting, result)
