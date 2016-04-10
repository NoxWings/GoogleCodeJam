#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# T9 message problem
#===============================================================================

from __future__ import unicode_literals
from codejam.common import CodeJamIO, Problem, ProblemInstance

#------------------------------------------------------------------------------


T9 = {
    ' ': '0',
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999'
}


class T9Message(ProblemInstance):

    def __init__(self):
        self.msg = CodeJamIO.read_input(strip=False)

    def solve(self):
        t9 = ''
        for l in self.msg:
            v = T9[l]
            t9 += ' ' + v if (t9 and t9[-1] == v[0]) else v
        return t9

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(T9Message)
    p.solve()
