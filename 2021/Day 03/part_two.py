"""
Advent of Code 2021
Day 3 - Binary Diagnostic (Part Two)
"""

import pandas as pd

with open("./input.txt", encoding="utf-8") as file:
    data = pd.DataFrame([list(i) for i in file.read().splitlines()])

oxygen = data.copy()
carbon = data.copy()

column = 0
while column < 12:
    oxygen_count = oxygen[column].mode()
    if len(oxygen_count) == 2:
        oxygen = oxygen.loc[oxygen[column] == "1"]
    else:
        if len(carbon) == 1:
            break
        try:
            oxygen = oxygen.loc[oxygen[column] == oxygen_count[0]]
        except (ValueError, KeyError):
            break
    column += 1

column = 0
while column < 12:
    carbon_count = carbon[column].mode()
    if len(carbon_count) == 2:
        carbon = carbon.loc[carbon[column] == "0"]
    else:
        if len(carbon) == 1:
            break
        try:
            carbon = carbon.loc[carbon[column] ==
                                str(abs(int(carbon_count[0])-1))]
        except (ValueError, KeyError):
            break
    column += 1

oxygen_rating = "".join(list(oxygen.iloc[0]))
carbon_rating = "".join(list(carbon.iloc[0]))
result = int(oxygen_rating, 2) * int(carbon_rating, 2)

print("Result =", result)
