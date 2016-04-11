#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Fractiles
# https://code.google.com/codejam/contest/6254486/dashboard#s=p3
#===============================================================================

from __future__ import unicode_literals
import math
from codejam.common import CodeJamIO, Problem, ProblemInstance

#------------------------------------------------------------------------------


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class Fractiles(ProblemInstance):

    def __init__(self):
        self.k, self.c, self.s = CodeJamIO.read_int_multi()
        self.k_pow_c = [pow(self.k, cs) for cs in xrange(self.c)]

    def solve(self):
        min_s = math.ceil(self.k / float(self.c))
        if self.s < min_s:
            return 'IMPOSSIBLE'

        level1 = range(self.k)
        solution_chunks = list(chunks(level1, self.c))
        solution = [self.compute_index(chunk) for chunk in solution_chunks]

        return ' '.join([str(x) for x in solution])

    def compute_index(self, chunk):
        # reverse order index
        chunk_contribution = [self.k_pow_c[idx] * e for idx, e in enumerate(reversed(chunk))]
        index = sum(chunk_contribution) + 1L
        return index

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(Fractiles)
    p.solve()
