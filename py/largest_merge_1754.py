#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def self_merge(s, t1, t2):
    # return the merge of s with itself.  t1 and t2 are the terminating characters of each string.

    b, s = max(t1, t2), min(t1, t2)
    if not s:
        return "%s%s" % (b, s)

    # ay, az ==> azay
    # ma, mz ==> mzma
    # mb, ma ==> mmba
    # abca, abcd ==> abcdabca
    # zyxz, zyxa ==> zzyyxxza



    result = ""


    return result


def solution(s1, s2):
    # identify the longest common prefix of each string.  then look ahead 1 char in each.
    # the biggest of these prefixes is appended to the result.
    #
    # 'a' precedes 'aa'.

    pprint(s1)
    pprint(s2)

    result = ""
    p1a = 0
    p2a = 0

    while p1a < len(s1) and p2a < len(s2):
        p1 = p1a
        p2 = p2a

        while p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1

        common_substring = s1[p1a:p1]
        pprint(common_substring)

        if p1 < len(s1) and p2 < len(s2):
            # we came to a character that stopped the traversal.  so we have common substrings (possibly 0 length)
            # followed by different characters.
            #
            # divide the common substring into descending and ascending parts.  for the descending parts,
            # add one char at a time from each.  don't add the last char of descenders.  for the ascending parts,
            # add the ascender terminated by the bigger
            # char, then the one terminated by the smaller char.  if the ascending parts are terminated by the
            # same char, don't add it.
            p1a = p1 + 1
            p2a = p2 + 1
        elif p1 < len(s1):
            result += s1[p1a:p1 + 1]
            p1a = p1 + 1
        else:
            result += s2[p2a:p2 + 1]
            p2a = p2 + 1

    if p1a < len(s1):
        result += s1[p1a:]
    elif p2a < len(s2):
        result += s2[p2a:]

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_0(self):
        s1 = ""
        s2 = ""
        expecting = ""
        self.assertEqual(expecting, solution(s1, s2))

    def test_1(self):
        s1 = "cabaa"
        s2 = "bcaaa"
        expecting = "cbcabaaaaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_2(self):
        s1 = "abcabc"
        s2 = "abdcaba"
        expecting = "abdcabcabcaba"
        self.assertEqual(expecting, solution(s1, s2))

    def test_3(self):
        s1 = "cabaa"
        s2 = ""
        expecting = "cabaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_4(self):
        s1 = ""
        s2 = "cabaa"
        expecting = "cabaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_5(self):
        s1 = "cabaa"
        s2 = "z"
        expecting = "zcabaa"
        self.assertEqual(expecting, solution(s1, s2))

    def test_6(self):
        s1 = "uuurr"
        s2 = "urrr"
        expecting = "uuuurrrrr"
        self.assertEqual(expecting, solution(s1, s2))

    def test_7(self):
        s1 = "uuurruuuruuuuuuuuruuuuu"
        s2 = "urrrurrrrrrrruurrrurrrurrrrruu"
        expecting = "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"
        self.assertEqual(expecting, solution(s1, s2))

    def test_8(self):
        s1 = "tpppprrppttppppppppappaprrpp"
        s2 = "tpptppppppptpppprprtpp"
        expecting = "ttpptpppprrppttppppppptpppprprtppppppppppappaprrpp"
        self.assertEqual(expecting, solution(s1, s2))

    def test_9(self):
        s1 = "edcbabcd"
        s2 = "edcbabcx"
        expecting = "eeddccbbabcxabcd"
        self.assertEqual(expecting, solution(s1, s2))

    def test_10(self):
        s1 = "edcbab"
        s2 = "edcbax"
        expecting = "eeddccbbaxab"
        self.assertEqual(expecting, solution(s1, s2))

    def test_11(self):
        s1 = "abcde"
        s2 = "abcdx"
        expecting = "abcdxabcde"
        self.assertEqual(expecting, solution(s1, s2))

