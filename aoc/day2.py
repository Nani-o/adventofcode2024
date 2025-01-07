#!/usr/bin/env python

import math

def part1(puzzle_input):
    reports = [list(map(int, x.strip().split(' '))) for x in puzzle_input.strip().split('\n')]
    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
    return safe_reports

def part2(puzzle_input):
    reports = [list(map(int, x.strip().split(' '))) for x in puzzle_input.strip().split('\n')]
    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
        else:
            for x in range(len(report)):
                if is_report_safe(report[:x] + report[x+1:]):
                    safe_reports += 1
                    break
    return safe_reports

def is_report_safe(report):
    distances = []
    last = report[0]
    for level in report[1::]:
        distances.append(level - last)
        last = level
    elements = len(distances)
    positives_distances = [x for x in distances if x > 0 and 1 <= abs(x) <= 3]
    negative_distances = [x for x in distances if x < 0 and 1 <= abs(x) <= 3]
    if len(positives_distances) == elements or len(negative_distances) == elements:
        return True
    return False
