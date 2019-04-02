#!/usr/bin/env python

# https://leetcode.com/problems/longest-substring-without-repeating-characters/?tab=Description

# Given a string, find the length of the longest substring without repeating characters.
# in case of a tie, earliest substring wins.

def nonrepeating_substring_at(s, p):
    # returns (p, length_of_substring_at_p)
    tally = set()
    substring_len = 0
    for c in s[p:]:
        if c in tally:
            break
        tally.add(c)
        substring_len += 1
    return (p, substring_len)

def mylen(l):
    return len(l)

def length_of_longest_substring(s):
    maxlen = 0
    # len will be evaluated just once
    for i in xrange(mylen(s)):
        idx, len_at_idx = nonrepeating_substring_at(s, i)
        maxlen = max(maxlen, len_at_idx)
    return maxlen

if __name__ == '__main__':
    trials = ['bbbbb', 'abcabcbb', 'pwwkew',
              'abcarxwy',
              ]
    for s in trials:
        print s, length_of_longest_substring(s)
