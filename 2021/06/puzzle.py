#!/usr/bin/env python3

import sys
from collections import namedtuple
from functools import reduce

input = sys.stdin.read().strip()
generation = [0] * 9
for i in input.split(","):
  generation[int(i)] += 1

def nextGeneration(generation):
  nextGeneration = [0] * 9
  for i, n in enumerate(generation):
    if i == 0:
      nextGeneration[6] = n
      nextGeneration[8] = n
    else:
      nextGeneration[i-1] += n
  return nextGeneration
def pop(generation, k):
  for i in range(k):
    generation = nextGeneration(generation)
  return sum(generation)

print("Part one:", pop(generation, 80))
print("Part two:", pop(generation, 256))
