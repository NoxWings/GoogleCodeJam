#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


#===============================================================================
# Input output useful function
#===============================================================================

class CodeJamIO:

    @staticmethod
    def read_input(strip=True):
        if strip:
            return raw_input().strip()
        else:
            return raw_input()

    @staticmethod
    def read_input_multi(strip=True):
        return CodeJamIO.read_input(strip).split(" ")

    @staticmethod
    def read_int():
        return int(CodeJamIO.read_input().strip())

    @staticmethod
    def read_int_multi():
        return [int(s) for s in CodeJamIO.read_input_multi()]

#===============================================================================
# Problem class
#===============================================================================


class Problem:

    def __init__(self, instance_type):
        self.test_cases = CodeJamIO.read_int()
        self.problem_instances = (instance_type() for _ in xrange(self.test_cases))

    def solve(self):
        for idx, problem_instance in enumerate(self.problem_instances):
            print("Case #{}: {}".format(idx + 1, problem_instance.solve()))


#===============================================================================
# Problem instance
#===============================================================================

class ProblemInstance:

    def solve(self):
        raise NotImplementedError()
