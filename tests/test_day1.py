#!/usr/bin/env python

import pytest
from aoc.day1 import part1, part2

def test_part1():
    input = """3   4
               4   3
               2   5
               1   3
               3   9
               3   3"""
    solution = part1(input)
    assert solution == 11

def test_part2():
    input = """3   4
               4   3
               2   5
               1   3
               3   9
               3   3"""
    solution = part2(input)
    assert solution == 31
