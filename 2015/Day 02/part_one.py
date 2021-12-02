"""
Advent of Code 2015
Day 2 - I Was Told There Would Be No Math (Part One)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().split("\n")

total = 0

for present in data:
    l, w, h = [int(i) for i in present.split("x")]
    s1 = l*w
    s2 = w*h
    s3 = h*l
    total += (2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3))

print("Result =", total)
