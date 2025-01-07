#!/usr/bin/env python

import pytest
from aoc.day2 import part1, part2

def test_part1():
    input = """7 6 4 2 1
               1 2 7 8 9
               9 7 6 2 1
               1 3 2 4 5
               8 6 4 4 1
               1 3 6 7 9"""
    solution = part1(input)
    assert solution == 2

def test_part2():
    input = """7 6 4 2 1
               1 2 7 8 9
               9 7 6 2 1
               1 3 2 4 5
               8 6 4 4 1
               1 3 6 7 9"""
    solution = part2(input)
    assert solution == 4
