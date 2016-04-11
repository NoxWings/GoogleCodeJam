#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Coin Jam
# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
#===============================================================================

from __future__ import unicode_literals

import random
from codejam.common import CodeJamIO


#------------------------------------------------------------------------------
def base10(n, b):
    digits = '0123456789ABCDEF'
    n = sum([digits.index(x) * pow(b, i) for i, x in enumerate(reversed(n))])
    return n


class CoinJam:

    def __init__(self):
        self.test_cases = CodeJamIO.read_int()
        self.n, self.j = CodeJamIO.read_int_multi()
        self.coins = set()
        self.max_divisor = 1000

    def random_coin(self):
        coin = '1' + ''.join([str(random.randrange(2)) for _ in range(self.n - 2)]) + '1'
        return coin if coin not in self.coins else self.random_coin()

    def get_divisors(self, coin):
        divisors = []
        for b in xrange(2, 11):
            n = base10(coin, b)
            for d in xrange(2, self.max_divisor):
                if d >= n:
                    break
                if (n % d) == 0:
                    divisors.append(d)
                    break
            if len(divisors) != (b - 1):
                break
        return divisors

    def solve(self):
        case = 1
        while len(self.coins) < self.j:
            coin = self.random_coin()
            divisors = self.get_divisors(coin)
            if (len(divisors) == 9):
                self.coins.add(coin)
                print('Case #{}: {} {}'.format(case, coin, ' '.join([str(d) for d in divisors])))
                case += 1

#------------------------------------------------------------------------------

if __name__ == '__main__':
    CoinJam().solve()
