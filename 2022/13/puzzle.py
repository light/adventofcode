#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

pairs = []
inp = inputs()
for l1 in inp:
  l2 = next(inp)
  pairs.append((eval(l1), eval(l2)))
  try:
    next(inp)
  except StopIteration:
    break

def compare(a, b):
  if type(a) is int and type(b) is int:
    return 1 if a > b else -1 if a < b else 0
  elif type(a) is int:
    return compare([a], b)
  elif type(b) is int:
    return compare(a, [b])
  else:
    for i in range(min(len(a), len(b))):
      c = compare(a[i], b[i])
      if c != 0:
        return c
    # first items compared equal
    if len(a) < len(b):
      return -1
    elif len(a) > len(b):
      return 1
    else:
      return 0


score1 = 0
for i, p in enumerate(pairs):
  if compare(*p) <= 0:
    score1 += i+1


print_res("Part one:", score1, 1)
