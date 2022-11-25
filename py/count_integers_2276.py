#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.icount = 0

    def setcount(self):
        total = 0
        for i in self.intervals:
            total += (i[1] - i[0] + 1)
        self.icount = total

    def add(self, left: int, right: int) -> None:
        newinterval = [left, right]
        # print("adding %s to %s" % (newinterval, self.intervals))
        if not self.intervals:
            self.intervals.append(newinterval)
            self.icount = right - left + 1
            return

        # optimizations first:  interval goes at the end or the beginning
        if right < self.intervals[0][0]:
            self.intervals = [newinterval] + self.intervals
            self.icount += (right - left + 1)
            return

        if left > self.intervals[-1][1]:
            self.intervals.append(newinterval)
            self.icount += (right - left + 1)
            return

        # get the indexes of the intervals that overlap
        i = 0
        overlap_range = []
        overlap_interval = newinterval
        for v in self.intervals:
            if v[0] <= newinterval[0] <= v[1]:
                overlap_range.append(i)
                overlap_interval = [v[0], max(v[1], overlap_interval[1])]
            elif newinterval[0] <= v[0] <= newinterval[1]:
                overlap_range.append(i)
                overlap_interval = [min(newinterval[0], overlap_interval[0]), max(v[1], overlap_interval[1])]
            elif overlap_range:
                break

            i += 1

        if overlap_range:
            # print("case 1:  %s, %s, %s" % (overlap_range, overlap_interval, self.intervals))
            self.intervals = self.intervals[:overlap_range[0]] + [overlap_interval] + self.intervals[
                                                                                      overlap_range[-1] + 1:]
        else:
            # there is no overlap.  find an insertion point and stick it in.
            put_it_here = 0
            while put_it_here < len(self.intervals) and self.intervals[put_it_here][0] <= newinterval[1]:
                put_it_here += 1
            self.intervals = self.intervals[:put_it_here] + [newinterval] + self.intervals[put_it_here:]
            # print("case 2:  %s" % self.intervals)

        self.setcount()

    def count(self) -> int:
        return self.icount


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_2(self):
        ci = CountIntervals()
        ci.add(3, 5)
        ci.add(1, 2)
        self.assertEqual(5, ci.count())
        ci.add(1, 10)
        self.assertEqual(10, ci.count())
        self.assertEqual([[1, 10]], ci.intervals)

    def test_1(self):
        ci = CountIntervals()
        ci.add(2, 3)
        ci.add(7, 10)
        # pprint(ci.intervals)
        self.assertEqual(6, ci.count())
        ci.add(5, 8)
        # pprint(ci.intervals)
        self.assertEqual(8, ci.count())

    def test_big(self):
        ci = CountIntervals()
        ci.add(365, 897)
        ci.add(261, 627)
        ci.add(781, 884)
        self.assertEqual(637, ci.count())
        self.assertEqual(637, ci.count())
        self.assertEqual(637, ci.count())
        ci.add(328, 495)
        ci.add(224, 925)
        ci.add(228, 464)
        self.assertEqual(702, ci.count())
        ci.add(416, 451)
        self.assertEqual(702, ci.count())
        ci.add(747, 749)
        self.assertEqual(702, ci.count())
        self.assertEqual(702, ci.count())
        self.assertEqual(702, ci.count())
        self.assertEqual(702, ci.count())
        self.assertEqual(702, ci.count())
        ci.add(740, 757)
        ci.add(51, 552)
        ci.add(20, 896)
        ci.add(459, 712)
        self.assertEqual(906, ci.count())
        ci.add(383, 670)
        self.assertEqual(906, ci.count())
        ci.add(701, 924)
        self.assertEqual(906, ci.count())
        self.assertEqual(906, ci.count())
        ci.add(392, 591)
        self.assertEqual(906, ci.count())
        self.assertEqual(906, ci.count())
        ci.add(935, 994)
        self.assertEqual(966, ci.count())
        self.assertEqual(966, ci.count())
        self.assertEqual(966, ci.count())
        ci.add(398, 525)
        ci.add(335, 881)
        ci.add(243, 517)
        self.assertEqual(966, ci.count())
        ci.add(995, 1000)
        ci.add(15, 335)
        ci.add(430, 490)
        ci.add(376, 681)
        self.assertEqual(977, ci.count())
        ci.add(733, 841)
        self.assertEqual(977, ci.count())
        self.assertEqual(977, ci.count())
        ci.add(603, 633)
        ci.add(974, 978)
        ci.add(466, 786)
        ci.add(241, 753)
        ci.add(259, 887)
        self.assertEqual(977, ci.count())
        self.assertEqual(977, ci.count())
        ci.add(410, 514)
        ci.add(173, 300)
        self.assertEqual(977, ci.count())
        self.assertEqual(977, ci.count())
        self.assertEqual(977, ci.count())
        ci.add(805, 957)
        ci.add(272, 805)
        ci.add(723, 858)
        ci.add(113, 118)
        self.assertEqual(986, ci.count())
        ci.add(426, 987)
        ci.add(318, 997)
        ci.add(741, 978)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(701, 992)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(562, 766)
        ci.add(987, 1000)
        self.assertEqual(986, ci.count())
        ci.add(929, 929)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(926, 931)
        ci.add(913, 975)
        self.assertEqual(986, ci.count())
        ci.add(930, 962)
        ci.add(707, 914)
        ci.add(688, 757)
        self.assertEqual(986, ci.count())
        ci.add(430, 433)
        ci.add(452, 683)
        ci.add(794, 919)
        ci.add(799, 991)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(658, 731)
        self.assertEqual(986, ci.count())
        ci.add(328, 686)
        ci.add(998, 999)
        self.assertEqual(986, ci.count())
        ci.add(455, 938)
        ci.add(981, 988)
        self.assertEqual(986, ci.count())
        ci.add(92, 699)
        ci.add(311, 690)
        ci.add(916, 920)
        self.assertEqual(986, ci.count())
        ci.add(213, 339)
        ci.add(605, 961)
        ci.add(719, 902)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(129, 833)
        self.assertEqual(986, ci.count())
        ci.add(844, 926)
        ci.add(940, 956)
        ci.add(148, 182)
        self.assertEqual(986, ci.count())
        ci.add(163, 885)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(532, 886)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(306, 906)
        self.assertEqual(986, ci.count())
        self.assertEqual(986, ci.count())
        ci.add(948, 963)
        self.assertEqual(986, ci.count())
        ci.add(116, 853)
