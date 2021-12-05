#!/usr/bin/env python3

import sys
from collections import namedtuple
from functools import reduce

P = namedtuple("P", ["x", "y"])
lines = []
bounds = [0, 0]
for l in sys.stdin:
  line = [P(*[int(c) for c in coords.split(",")]) for coords in l.split(" -> ")]
  # Make our job easier later by making sure line is in increasing X order
  if line[0].x > line[1].x:
    line[:] = line[::-1]
  lines.append(line)
  for p in line:
    bounds[0] = max(bounds[0], p.x)
    bounds[1] = max(bounds[1], p.y)
vents = [[0] * (bounds[1]+1) for x in range(bounds[0]+1)]

def ventrange(a, b):
  if a > b:
    return range(b, a+1)
  return range(a, b+1)

for l in lines:
  if l[0].x == l[1].x:
    for y in ventrange(l[0].y, l[1].y):
      vents[l[0].x][y] += 1
  if l[0].y == l[1].y:
    for x in ventrange(l[0].x, l[1].x):
      vents[x][l[0].y] += 1

def nb_overlaps(vents):
  return sum([reduce(lambda a, b: a+1 if b >=2 else a, ly, 0) for ly in vents])

print("Part one:", nb_overlaps(vents))

for l in lines:
  if l[0].x != l[1].x and l[0].y != l[1].y:
    y_step = 1 if l[1].y > l[0].y else -1
    y = l[0].y
    for x in ventrange(l[0].x, l[1].x):
      vents[x][y] += 1
      y += y_step

print("Part two:", nb_overlaps(vents))
