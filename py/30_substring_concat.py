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


def visit(text, positions_to_words, word_counts, all_indices, fromhere, nwords):
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

    matches = re.finditer("|".join(unique_words), text)
    for m in matches:
        span = m.span()
        substring = text[span[0]:span[1]]
        positions_to_words[span[0]] = substring
        all_indices.append(span[0])

    # maybe we don't need to do this
    sorted(all_indices)

    # TODO - all_indices might be empty

    result = []
    for i in range(len(all_indices) - len(words) + 1):
        r = visit(text, positions_to_words, word_counts, all_indices, i, len(words))
        if r is not None:
            result.append(r)

    if result:
        return result


if __name__ == '__main__':
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]

    result = solution(s, words)
    pprint(result)


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
        self.assertIsNone(result)

