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


def y_intercept(p, slope):
    return p[1] - slope * p[0]


def solution(points):
    non_vertical_lines = {}  # maps (m, b) to list of points
    vertical_lines = {}  # maps x intercept to list of points

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            m = slope(points[i], points[j])
            b = y_intercept(points[i], points[j])
            if m is None:
                x_int = points[i][0]
                if x_int not in vertical_lines:
                    vertical_lines[x_int] = []
                vertical_lines[x_int].append(tuple(points[i]))
                vertical_lines[x_int].append(tuple(points[j]))
            else:
                if (m, b) not in non_vertical_lines:
                    non_vertical_lines[(m, b)] = []
                non_vertical_lines[(m, b)].append(tuple(points[i]))
                non_vertical_lines[(m, b)].append(tuple(points[j]))

    max_points = 0
    for k in non_vertical_lines.keys():
        non_vertical_lines[k] = set(non_vertical_lines[k])
        max_points = max(max_points, len(non_vertical_lines[k]))

    for k in vertical_lines.keys():
        vertical_lines[k] = set(vertical_lines[k])
        max_points = max(max_points, len(vertical_lines[k]))

    return max_points


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        expected = 4
        self.assertEqual(expected, solution(points))

        