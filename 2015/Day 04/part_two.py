"""
Advent of Code 2015
Day 4: The Ideal Stocking Stuffer (Part Two)
"""

import hashlib

with open("./input.txt", encoding="utf-8") as file:
    data = file.read()


def format_hash(secret, number) -> str:
    return f"{secret}{number}".encode()


value = 0

while True:
    hashed = hashlib.md5(format_hash(data, value))
    if hashed.hexdigest().startswith("000000"):
        break
    value += 1

print("Result =", value)
