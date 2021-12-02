"""
Advent of Code 2015
Day 2 - I Was Told There Would Be No Math (Part Two)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().split("\n")

total = 0

for present in data:
    l, w, h = [int(i) for i in present.split("x")]
    ribbon = 2 * (l + w + h - max(l, w, h))
    bow = l * w * h
    total += ribbon + bow

print("Result =", total)
