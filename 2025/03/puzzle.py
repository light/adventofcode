#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

banks = [l for l in inputs()]

score1 = 0

for bank in banks:
  i1 = None
  for i in range(len(bank) - 2, -1, -1):
    d = bank[i]
    if i1 is None or d >= bank[i1]:
      i1 = i
  i2 = None
  for i in range(i1+1, len(bank)):
    d = bank[i]
    if i2 is None or d > bank[i2]:
      i2 = i
  j = bank[i1]+bank[i2]
  score1 += int(j)

print_res("Part one:", score1, 1)

