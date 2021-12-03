#!/usr/bin/env python3

import sys

def count_bit(lines, bit):
  ones = 0
  n = 0
  for line in lines:
    if line[bit] == "1":
      ones += 1
    n += 1
  return (ones, n)
def most_bit(lines, bit):
  ones, n = count_bit(lines, bit)
  return "1" if ones >= n/2 else "0"
def least_bit(lines, bit):
  ones, n = count_bit(lines, bit)
  return "0" if ones >= n/2 else "1"

linesA = sys.stdin.read().splitlines()
linesB = linesA

i = 0
while len(linesA) > 1:
  bit = most_bit(linesA, i)
  linesA = [l for l in linesA if l[i] == bit]
  i += 1

i = 0
while len(linesB) > 1:
  bit = least_bit(linesB, i)
  linesB = [l for l in linesB if l[i] == bit]
  i += 1

oxygen = int(linesA[0], 2)
co2 = int(linesB[0], 2)

print(oxygen*co2)