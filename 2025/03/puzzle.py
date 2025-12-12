#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

banks = [l for l in inputs()]


def find_greatest(bank):
  imax = None
  for i in range(len(bank)):
    d = bank[i]
    if imax is None or d > bank[imax]:
      imax = i
  return imax

def max_joltage(bank, n):
  istart = 0
  digits = []
  for k in range(n):
    i = find_greatest(bank[istart:len(bank)-(n-k)+1]) + istart
    digits.append(bank[i])
    istart = i+1
  return int("".join(digits))

score1 = sum(max_joltage(bank, 2) for bank in banks)
score2 = sum(max_joltage(bank, 12) for bank in banks)

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
