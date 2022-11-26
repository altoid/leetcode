#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


class MyCalendarThree:

    def __init__(self):
        self.intervals = []
        self.intervals_to_counts = {}
        self.max_booking = 0

    def overlaps(self, i1, i2):
        if i1[0] <= i2[0] < i1[1]:
            return True
        if i2[0] <= i1[0] < i2[1]:
            return True
        return False

    def find_intersections(self, overlap_range, newinterval):
        intersections = [min(newinterval[0], self.intervals[overlap_range[0]][0])]

        if len(overlap_range) == 1:
            p1 = min(newinterval[0], self.intervals[0][0])
            p2 = max(newinterval[0], self.intervals[0][0])
            p3 = min(newinterval[1], self.intervals[0][1])
            p4 = max(newinterval[1], self.intervals[0][1])
            if p1 > intersections[-1]:
                intersections.append(p1)
            if p2 > intersections[-1]:
                intersections.append(p2)
            if p3 > intersections[-1]:
                intersections.append(p3)
            if p4 > intersections[-1]:
                intersections.append(p4)
            return intersections

        r = overlap_range[0]
        p1 = min(newinterval[0], self.intervals[r][0])
        p2 = max(newinterval[0], self.intervals[r][0])
        p3 = self.intervals[r][1]
        if p1 > intersections[-1]:
            intersections.append(p1)
        if p2 > intersections[-1]:
            intersections.append(p2)
        if p3 > intersections[-1]:
            intersections.append(p3)

        for r in overlap_range[1:-1]:
            p1 = self.intervals[r][0]
            p2 = self.intervals[r][1]

            if p1 > intersections[-1]:
                intersections.append(p1)
            if p2 > intersections[-1]:
                intersections.append(p2)

        r = overlap_range[-1]
        p1 = self.intervals[r][0]
        p2 = min(newinterval[1], self.intervals[r][1])
        p3 = max(newinterval[1], self.intervals[r][1])

        if p1 > intersections[-1]:
            intersections.append(p1)
        if p2 > intersections[-1]:
            intersections.append(p2)
        if p3 > intersections[-1]:
            intersections.append(p3)

        return intersections

    def book(self, start, end):
        # has to return the largest k anywhere in the calendar, not just
        # imparted by this interval.
        # intervals are open.

        newinterval = (start, end)
        if not self.intervals:
            self.intervals.append(newinterval)
            self.max_booking = 1
            self.intervals_to_counts[newinterval] = 1
            return self.max_booking

        # optimizations first:  interval goes at the end or the beginning
        if end < self.intervals[0][0]:
            self.intervals = [newinterval] + self.intervals
            self.intervals_to_counts[newinterval] = 1
            return self.max_booking

        if start >= self.intervals[-1][1]:
            self.intervals.append(newinterval)
            self.intervals_to_counts[newinterval] = 1
            return self.max_booking

        # get the indexes of the intervals that overlap
        i = 0
        overlap_range = []
        for v in self.intervals:
            if self.overlaps(v, newinterval):
                overlap_range.append(i)
            elif overlap_range:
                break

            i += 1

        if not overlap_range:
            # there is no overlap.  find an insertion point and stick it in.
            put_it_here = 0
            while put_it_here < len(self.intervals) and self.intervals[put_it_here][0] < newinterval[1]:
                put_it_here += 1
            self.intervals = self.intervals[:put_it_here] + [newinterval] + self.intervals[put_it_here:]
            self.intervals_to_counts[newinterval] = 1
            self.max_booking = max(self.max_booking, 1)
        else:
            # find all the intersection points of new interval with the existing intervals.
            intersections = self.find_intersections(overlap_range, newinterval)
            if len(intersections) > 1:
                # go through consecutive pairs in intersections and see what they intersect with.
                i = 0
                o = 0
                current = self.intervals[overlap_range[o]]
                new_segments = []
                while i < len(intersections) - 1:
                    k = 0
                    segment = (intersections[i], intersections[i + 1])
                    if segment[0] >= current[1]:
                        if o + 1 < len(overlap_range):
                            o += 1
                            current = self.intervals[overlap_range[o]]

                    new_segments.append(segment)
                    if self.overlaps(segment, newinterval):
                        k += 1
                    if self.overlaps(segment, current):
                        k += self.intervals_to_counts[current]
                    if segment not in self.intervals_to_counts:
                        self.intervals_to_counts[segment] = 0
                    self.intervals_to_counts[segment] = k
                    self.max_booking = max(self.max_booking, self.intervals_to_counts[segment])
                    i += 1

                # replace the range of overlapped segments with the new ones
                new_intervals = self.intervals[:overlap_range[0]] + new_segments + self.intervals[overlap_range[-1] + 1:]

                # don't remove the old overlapped intervals from the dictionary.  it's messy and leaving them
                # in won't affect the result

                self.intervals = new_intervals

        return self.max_booking


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_2(self):
        mc3 = MyCalendarThree()

        self.assertEqual(1, mc3.book(0, 2))
        self.assertEqual(1, mc3.book(4, 7))
        self.assertEqual(1, mc3.book(8, 10))
        self.assertEqual(1, mc3.book(11, 12))
        self.assertEqual(1, mc3.book(12, 16))

        self.assertEqual(2, mc3.book(5, 14))

    def test_1(self):
        mc3 = MyCalendarThree()
        self.assertEqual(1, mc3.book(10, 20))
        self.assertEqual(1, mc3.book(50, 60))
        self.assertEqual(2, mc3.book(10, 40))
        self.assertEqual(3, mc3.book(5, 15))
        self.assertEqual(3, mc3.book(5, 10))
        self.assertEqual(3, mc3.book(25, 55))

