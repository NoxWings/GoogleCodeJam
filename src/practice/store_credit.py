#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Store credit problem
#===============================================================================

from __future__ import unicode_literals
from codejam.common import CodeJamIO, Problem, ProblemInstance


#------------------------------------------------------------------------------

class StoreCredit(ProblemInstance):

    def __init__(self):
        self.credit = CodeJamIO.read_int()
        self.store_items = CodeJamIO.read_int_multi()
        self.items = CodeJamIO.read_int_multi()

    def solve(self):
        permutations = (('{} {}'.format(idx + 1, idy + 1), x + y)
                        for idx, x in enumerate(self.items)
                        for idy, y in enumerate(self.items)
                        if idx < idy)

        permutations = [x for x in permutations]

        best_remaining = self.credit
        best_pair = None
        for pair, val in permutations:
            remaining = self.credit - val
            if remaining < 0:
                continue
            elif remaining == 0:
                return pair
            else:
                if (remaining < best_remaining):
                    best_remaining = remaining
                    best_pair = pair

        return best_pair

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(StoreCredit)
    p.solve()
