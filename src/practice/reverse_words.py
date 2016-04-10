#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Revere words problem
#===============================================================================

from __future__ import unicode_literals
from codejam.common import CodeJamIO, Problem, ProblemInstance


#------------------------------------------------------------------------------

class ReverseWords(ProblemInstance):

    def __init__(self):
        self.words = CodeJamIO.read_input_multi()

    def solve(self):
        return ' '.join(self.words[::-1])

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(ReverseWords)
    p.solve()
