#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Revenge of the Pancakes
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#===============================================================================

from __future__ import unicode_literals
from codejam.common import CodeJamIO, Problem, ProblemInstance

#------------------------------------------------------------------------------


def clean(p):
    """Remove happy endings"""
    while p and p[-1]:
        p = p[:-1]
    return p


def count_consecutive(p, val):
    count = 0
    for x in p:
        if x != val:
            break
        count += 1
    return count


class Pancakes(ProblemInstance):

    def __init__(self):
        self.p = CodeJamIO.read_input()

    def solve(self):
        def count_steps(p):
            p = clean(p)
            if not p:
                return 0
            left = count_consecutive(p, False)
            right = count_consecutive(reversed(p), False)
            if left >= right:
                p = [not c for c in reversed(p)]
                return count_steps(p) + 1
            else:
                # No list reverse
                p = [not c for c in p[:-right]]
                return count_steps(p) + 1

        p = [True if c == '+' else False for c in self.p]
        steps = count_steps(p)
        return steps

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(Pancakes)
    p.solve()
