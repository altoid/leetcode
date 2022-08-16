#!/usr/bin/env python3

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

import unittest
from functools import reduce


def rlc_reducer(acc, next_char):
    # the second arg to a reducer is not the rest of the input, just the first
    # element of the rest of the input

    t = (next_char, 1)
    if acc and acc[-1][0] == next_char:
        t = (next_char, acc[-1][1] + 1)
        acc.pop()

    acc.append(t)

    return acc
    

def run_length_encode(s):
    return reduce(rlc_reducer, s, [])


def decode(e):
    """
    given a run-length encoding, produce the original string
    """
    return ''.join([x[0] * x[1] for x in e])

    
def compact_reducer(acc, next_tuple):
    new_t = next_tuple
    
    if acc:
        tail = acc[-1]
        if tail[0] == new_t[0]:
            new_t = (tail[0], tail[1] + new_t[1])
            acc.pop()

    acc.append(new_t)
    return acc

def compact_encoding(e):
    """
    to be called after removing a chunk from the string, coalesces adjacent remnants.

    for example, given this:

    [('a', 1), ('b', 2), ('c', 3), ('b', 2), ('a', 1), ('c', 2), ('b', 2)]

    if we remove the third element, we get this:

    [('a', 1), ('b', 2), ('b', 2), ('a', 1), ('c', 2), ('b', 2)]
               ^^^^^^^^^^^^^^^^^^
    
    the compaction step gives us this:

    [('a', 1), ('b', 4), ('a', 1), ('c', 2), ('b', 2)]

    """
    return reduce(compact_reducer, e, [])


def remove_duplicates(s, k):
    """
    remove runs of any character that are a multiple of k in length.
    """
    
    rle = run_length_encode(s)

    removed = [x for x in rle if x[1] % k != 0]

    while rle != removed:
        rle = compact_encoding(removed)
        removed = [x for x in rle if x[1] % k != 0]

    return decode(removed)


class MyTest(unittest.TestCase):
    def test1(self):
        s = 'abbcccbbaccbb'
        result = run_length_encode(s)
        self.assertEqual([('a', 1), ('b', 2), ('c', 3), ('b', 2), ('a', 1), ('c', 2), ('b', 2)], result)

        # remove the ('c', 3) element
        new_result = result[:2] + result[3:]
        new_result = compact_encoding(new_result)
        self.assertEqual([('a', 1), ('b', 4), ('a', 1), ('c', 2), ('b', 2)], new_result)

        self.assertEqual('abbbbaccbb', decode(new_result))
        
    def test2(self):
        s = 'pbbcggttciiippooaais'
        new_s = remove_duplicates(s, 2)
        self.assertEqual('ps', new_s)
        
    def test3(self):
        s = 'deeedbbcccbdaa'
        new_s = remove_duplicates(s, 3)
        self.assertEqual('aa', new_s)
        
    def test4(self):
        s = 'abcd'
        new_s = remove_duplicates(s, 2)
        self.assertEqual(s, new_s)
                
    def test5(self):
        s = 'azxxzy'
        new_s = remove_duplicates(s, 2)
        self.assertEqual('ay', new_s)
        
    
