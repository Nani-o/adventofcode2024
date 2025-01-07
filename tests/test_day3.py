#!/usr/bin/env python

import pytest
from aoc.day3 import part1, part2

def test_part1():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    solution = part1(input)
    assert solution == 161

def test_part2():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    solution = part2(input)
    assert solution == 48
