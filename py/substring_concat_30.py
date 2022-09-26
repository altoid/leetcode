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


class Solution(object):
    def __init__(self, text, words):
        self.text = text
        self.words = words
        self.total_word_length = sum([len(x) for x in words])
        self.hopeless = False

        # count the number of times each word is to appear in a correct substring
        self.word_counts = {}
        for w in self.words:
            if w not in self.word_counts:
                self.word_counts[w] = 0
            self.word_counts[w] += 1

        # optimization - if some word doesn't appear at all in the text, there's no way any permutation can exist.
        words_in_text = {}
        for w in self.words:
            if w not in words_in_text:
                words_in_text[w] = 0

        # get the index of each word as it appears in the text.  create a list of all indexes,
        # an a mapping of indexes to words.

        # create a list of unique words; shake out dups.
        unique_words = list(set(self.words))
        self.all_indices = []
        self.positions_to_words = {}


        pattern = "|".join(unique_words)
        pattern = "(?=(%s))" % pattern
        matches = re.finditer(pattern, self.text)
        for m in matches:
            span = m.start(1), m.end(1)
            substring = text[span[0]:span[1]]
            self.positions_to_words[span[0]] = substring
            self.all_indices.append(span[0])
            words_in_text[substring] += 1

        # if some word doesn't appear in the text, there is no solution
        for v in words_in_text.values():
            if v == 0:
                self.hopeless = True
                break

        # maybe we don't need to do this
        sorted(self.all_indices)

    #
    # we have to do a lot of work to handle this case:
    #
    # s = aaaaaaaaaaaaaa
    # words = [aa, aa]
    #
    # because of this, adjacent indices may be closer together than the length of any word.
    #
    def visit(self, fromhere):
        """
        fromhere is an index into all_indices.

        what we know:
        - it is possible for a permutation to fit starting at text[all_indices[fromhere]]
        - some permutation exists in the text
        """

        ledger = {}
        for w in self.word_counts.keys():
            ledger[w] = 0

        # we know there is a word it text[all_indices[fromhere]], and we know what it is.
        word = self.positions_to_words[self.all_indices[fromhere]]
        ledger[word] += 1

        idx_after_word = self.all_indices[fromhere] + len(word)

        for i in range(len(self.all_indices) - fromhere):
            if self.all_indices[fromhere + i] < idx_after_word:
                continue

            if self.all_indices[fromhere + i] > idx_after_word:
                return None

            # are we here?  then self.all_indices[fromhere + i] == idx_after_word
            # so the next word is adjacent to this one

            word = self.positions_to_words[self.all_indices[fromhere + i]]
            ledger[word] += 1
            if ledger[word] > self.word_counts[word]:
                return None

            # if we placed all the words, we can stop.
            done = True
            for w in self.words:
                if ledger[w] < self.word_counts[w]:
                    done = False
                    break

            if done:
                break

            idx_after_word = self.all_indices[fromhere + i] + len(word)

        for w in self.words:
            if ledger[w] < self.word_counts[w]:
                return None

        return self.all_indices[fromhere]

    def solve(self):
        result = []
        if self.hopeless:
            return result

        for i in range(len(self.all_indices)):
            if len(self.text) - self.all_indices[i] >= self.total_word_length:
                # visit at each index that leaves enough room to fit a permutation
                r = self.visit(i)
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
        # print(m.span())
        print(m)

    # matches = re.findall(pattern, s)
    # pprint(matches)


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaa"
    pattern = r'(?=(aa))'

    # futz("aaaaaaaaaaaaaa", r'(?=(aa))')
    futz("aaaaabbbbb", r'(?=(aa|bb))')
    # futz("aaaaabbbbb", r'(aa|bb)')

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
        solution = Solution(s, words)
        expecting = {6, 9, 12}
        result = set(solution.solve())
        self.assertEqual(expecting, result)

    def test_2(self):
        s = "barfoofoobarthefoobarman"
        words = ["mairzy", "doates", "pickle"]
        solution = Solution(s, words)
        result = solution.solve()
        expecting = []
        self.assertEqual(expecting, result)

    def test_3(self):
        s = "barfoofooxbarxthefoobarman"
        words = ["bar", "foo", "the"]
        solution = Solution(s, words)
        expecting = {14}
        result = set(solution.solve())
        self.assertEqual(expecting, result)

    def test_4(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the", "foo"]
        solution = Solution(s, words)
        expecting = {3, 6}
        result = set(solution.solve())
        self.assertEqual(expecting, result)

    def test_5(self):
        s = "barfoothefoobarman"
        words = ["bar", "foo"]
        solution = Solution(s, words)
        expecting = {9, 0}
        result = set(solution.solve())
        self.assertEqual(expecting, result)

    def test_6(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        solution = Solution(s, words)
        expecting = []
        result = solution.solve()
        self.assertEqual(expecting, result)

    def test_7(self):
        s = "aaaaaaaaaaaaaa"  # len == 14
        words = ["aa", "aa"]
        solution = Solution(s, words)
        expecting = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        result = set(solution.solve())
        self.assertEqual(expecting, result)

    def test_8(self):
        s = "aaaaa"
        words = ["aaaaaaaaa"]
        solution = Solution(s, words)
        expecting = []
        result = solution.solve()
        self.assertEqual(expecting, result)
