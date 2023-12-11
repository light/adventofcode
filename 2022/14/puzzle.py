#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from board import Board, P


cave = Board('.')
formations = []
for l in inputs():
  formations.append([list(map(int, p.split(","))) for p in l.split(" -> ")])
xmin, ymax = None, None
for points in formations:
  for p in points:
    xmin = p[0] if xmin is None else min(xmin, p[0])
    ymax = p[1] if ymax is None else max(ymax, p[1])
cave.shift(xmin, 0)
for points in formations:
  for i, p1 in enumerate(points[:-1]):
    p2 = points[i+1]
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    if dy == 0:
      x0 = min(p2[0], p1[0])
      for x in range(abs(dx)+1):
        cave.set(x0+x, p1[1], "#")
    else:
      y0 = min(p2[1], p1[1])
      for y in range(abs(dy)+1):
        cave.set(p1[0], y0+y, "#")

cave.set(500, 0, "+")
pour_point = cave.getP(500, 0)
# Add 1 tile amrgin for pouring
cave.extend_shift(left = 1, right = 1); cave.shift(-1, 0)
cave.print()

def drop_sand():
  x, y = pour_point.x, pour_point.y
  while y < ymax:
    if cave.get(x, y+1) == ".":
      y += 1
    elif cave.get(x-1, y+1) == ".":
      y += 1
      x -= 1
    elif cave.get(x+1, y+1) == ".":
      y += 1
      x += 1
    else:
      cave.set(x, y, "o")
      return
  return "abyss"

def drop_max_sand():
  count = 0
  while True:
    res = drop_sand()
    if res == "abyss":
      break
    count += 1
  cave.print()
  return count

score1 = drop_max_sand()
print_res("Part one:", score1, 1)

