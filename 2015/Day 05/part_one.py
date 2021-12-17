"""
Advent of Code 2015
Day 5: Doesn't He Have Intern-Elves For This? (Part One)
"""

import re

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().splitlines()

nice = 0
disallowed = r"ab|cd|pq|xy"
vowels = r"[aeiou]"
double = r"(.)\1"

for string in data:
    if len(re.findall(disallowed, string)) != 0:
        continue
    
    vowel_count = len(re.findall(vowels, string))
    if vowel_count < 3:
        continue
    
    if len(re.findall(double, string)) == 0:
        continue

    nice += 1

print("Result =", nice)
