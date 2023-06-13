#!/usr/bin/env python

import unittest
from pprint import pprint
import random
from math import isqrt


def get_row(board, n):
    r = board[n]
    r = [x for x in filter(lambda x: x != '.', r)]

    return r


def get_column(board, n):
    c = [board[i][n] for i in range(len(board[0]))]
    c = [x for x in filter(lambda x: x != '.', c)]
    print(c)
    return c


def get_box(board, r, c):
    d = isqrt(len(board))
    box = []
    for i in range(d):
        for j in range(d):
            box.append(board[r + i][c + j])

    box = [x for x in filter(lambda x: x != '.', box)]
    #print(box)
    return box


def solution(board):
    for i in range(len(board)):
        r = get_row(board, i)
        r_set = set(r)
        if len(r) != len(r_set):
            return False

    for i in range(len(board[0])):
        r = get_column(board, i)
        r_set = set(r)
        if len(r) != len(r_set):
            return False

    d = isqrt(len(board))
    for i in range(0, len(board), d):
        for j in range(0, len(board), d):
            box = get_box(board, i, j)
            box_set = set(box)
            if len(box) != len(box_set):
                return False

    return True


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertTrue(solution(board))

    def test_2(self):
        board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertFalse(solution(board))

    def test_3(self):
        board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                 [".", ".", ".", "5", "6", ".", ".", ".", "."],
                 ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                 [".", ".", ".", "7", ".", ".", ".", ".", "."],
                 [".", ".", ".", "5", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."]]

        self.assertFalse(solution(board))
