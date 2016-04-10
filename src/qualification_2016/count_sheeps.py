#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Counting Sheep
# https://code.google.com/codejam/contest/6254486/dashboard#s=p0
#===============================================================================

from __future__ import unicode_literals
from codejam.common import CodeJamIO, Problem, ProblemInstance

#------------------------------------------------------------------------------


class CountSheeps(ProblemInstance):

    def __init__(self):
        self.n = CodeJamIO.read_int()

    def solve(self):
        if self.n == 0:
            return 'INSOMNIA'

        digits2 = set()
        n = 0
        while len(digits2) != 10:
            n += self.n
            for d in str(n):
                digits2.add(d)

        return '{}'.format(n)

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(CountSheeps)
    p.solve()
