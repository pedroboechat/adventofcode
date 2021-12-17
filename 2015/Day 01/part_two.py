"""
Advent of Code 2015
Day 1: Not Quite List (Part Two)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read()

floor = 0

for index in range(len(data)):
    if data[index] == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        result = index + 1
        break

print("Result =", result)
