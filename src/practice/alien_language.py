#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Alien language problem
#===============================================================================

from __future__ import unicode_literals
import re
from codejam.common import Problem, ProblemInstance, CodeJamIO


#------------------------------------------------------------------------------

class AlienProblem(Problem):

    def __init__(self, instance_type):
        self.l, self.d, self.test_cases = CodeJamIO.read_int_multi()
        self.words = [CodeJamIO.read_input() for _ in xrange(self.d)]
        self.problem_instances = (instance_type(self.words) for _ in xrange(self.test_cases))


class AlienLanguage(ProblemInstance):

    def __init__(self, words):
        self.words = words
        self.msg = CodeJamIO.read_input(strip=False)
        self.regex = re.compile(self.msg.replace('(', '[').replace(')', ']'))

    def solve(self):
        count = 0
        for word in self.words:
            if self.regex.match(word):
                count += 1
        return str(count)

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = AlienProblem(AlienLanguage)
    p.solve()
