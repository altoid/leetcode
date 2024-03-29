#!/usr/bin/env python

import unittest
from pprint import pprint
import random

"""
idea - bucketize each pair of line segments by slope and y-intercept.  biggest bucket wins.  special-case
x = c.
"""


def slope(a, b):
    if a[0] == b[0]:
        return None

    return (b[1] - a[1]) / (b[0] - a[0])


def y_intercept(p, m):
    return p[1] - m * p[0]


def solution(points):
    if len(points) == 1:
        return 1

    points = list(map(tuple, points))
    non_vertical_lines = {}  # maps (m, b) to list of points
    vertical_lines = {}  # maps x intercept to list of points

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            m = slope(points[i], points[j])
            if m is None:
                x_int = points[i][0]
                if x_int not in vertical_lines:
                    vertical_lines[x_int] = set()
                vertical_lines[x_int].add(points[i])
                vertical_lines[x_int].add(points[j])
            else:
                b = y_intercept(points[i], m)
                if (m, b) not in non_vertical_lines:
                    non_vertical_lines[(m, b)] = set()
                non_vertical_lines[(m, b)].add(points[i])
                non_vertical_lines[(m, b)].add(points[j])

    max_points = 0
    for k in non_vertical_lines.keys():
        #non_vertical_lines[k] = set(non_vertical_lines[k])
        max_points = max(max_points, len(non_vertical_lines[k]))

    for k in vertical_lines.keys():
        #vertical_lines[k] = set(vertical_lines[k])
        max_points = max(max_points, len(vertical_lines[k]))

    return max_points


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_2(self):
        points = [[1, 1], [2, 2], [3, 3]]
        expected = 3
        self.assertEqual(expected, solution(points))

    def test_1(self):
        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        expected = 4
        self.assertEqual(expected, solution(points))
