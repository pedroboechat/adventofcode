"""
Advent of Code 2015
Day 5 - Doesn't He Have Intern-Elves For This? (Part Two)
"""

import re

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().splitlines()

nice = 0
pair = r"(.{2})"
double = r"(.)\1"

for string in data:
    has_pair = False
    for index in range(len(string)-1):
        if string.count(string[index:index+2]) > 1:
            has_pair = True
            break
    if not has_pair:
        continue

    s1 = string[::2]
    s2 = string[1::2]
    if len(re.findall(double, s1)) != 0 or len(re.findall(double, s2)) != 0:
        nice += 1

print("Result =", nice)
