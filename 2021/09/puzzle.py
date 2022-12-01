#!/usr/bin/env python3

import sys
from collections import namedtuple

P = namedtuple("P", ["x", "y"])

floor = []
for l in sys.stdin:
  floor.append([int(i) for i in l.strip()])
w = len(floor[0])
h = len(floor)

def neighbors(p):
  n = []
  if p.x != 0:
    n.append(P(p.x-1, p.y))
  if p.x != w-1:
    n.append(P(p.x+1, p.y))
  if p.y != 0:
    n.append(P(p.x, p.y-1))
  if p.y != h-1:
    n.append(P(p.x, p.y+1))
  return n
def height(p):
  return floor[p.y][p.x]
def is_low_point(x, y):
  p = floor[y][x]
  return ( (x == 0 or p < floor[y][x-1])
           and (x == w-1 or p < floor[y][x+1])
           and (y == 0 or p < floor[y-1][x])
           and (y == h-1 or p < floor[y+1][x]) )
def risk_level(p):
  return floor[p.y][p.x] + 1

low_points = [P(x, y) for y in range(h) for x in range(w) if is_low_point(x, y)]
def high_neighbors(p):
  return [n for n in neighbors(p) if (height(n) != 9 and height(n) > height(p))]
def basin(p, done_points):
  basin_points = {p}
  done_points.add(p)
  for n in high_neighbors(p):
    if n not in done_points:
      basin_points.add(n)
      basin_points.update(basin(n, done_points))
  return basin_points


print("Part one:", sum([risk_level(p) for p in low_points]))
largest = sorted([len(basin(p, set())) for p in low_points])
print("Part two:", largest[-1]*largest[-2]*largest[-3])