"""
Advent of Code 2021
Day 2: Dive! (Part One)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().splitlines()

horizontal = 0
depth = 0

for measurement in data:
    command, amount = measurement.split(" ")
    amount = int(amount)
    if command == "forward":
        horizontal += amount
    elif command == "down":
        depth += amount
    else:
        depth -= amount

result = horizontal * depth

print("Result =", result)
