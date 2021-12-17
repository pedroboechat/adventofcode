"""
Advent of Code 2015
Day 1: Not Quite List (Part One)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read()

floor = 0

for i in data:
    if i == "(":
        floor += 1
    else:
        floor -= 1

print("Result =", floor)
