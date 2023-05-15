#!/usr/bin/env python

# approach - for each point, calculate euclidean distance.  map distances to points.  maintain a sorted
# list of distances.  start from the beginning and spew points until we output k of them.  the terms of the problem
# imply that we will output all points for a candidate distance.

# another idea:  keep the points in a heap according to distance.  pop the first k of them.
# but python heaps don't let you order heaps with an arbitrary function.

import unittest
from pprint import pprint
import random
import math


def solution(points, k):
    result = []

    distance_to_points = {}

    for p in points:
        d = math.sqrt(p[0] * p[0] + p[1] * p[1])
        if d not in distance_to_points:
            distance_to_points[d] = []
        distance_to_points[d].append(p)

    distances = sorted([x for x in distance_to_points.keys()])

    kc = 0
    for d in distances:
        for p in distance_to_points[d]:
            result.append(p)
            kc += 1
            if kc >= k:
                break
        if kc >= k:
            break

    return result


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        pass
