"""
Advent of Code 2021
Day 1: Sonar Sweep (Part One)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = [int(i) for i in file.read().splitlines()]

previous = data[0]
increases = 0

for measurement in data[1:]:
    if measurement > previous:
        increases += 1
    previous = measurement

print("Result =", increases)
