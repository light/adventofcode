#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P
from path import a_star

universe = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    universe.set(x, y, v)

# Expand Universe
for y in range(universe.h-1, -1, -1):
  all_empty = True
  for x in range(universe.w):
    if universe.get(x, y) != ".":
      all_empty = False
      break
  if all_empty:
    universe.insertRow(y)
for x in range(universe.w-1, -1, -1):
  all_empty = True
  for y in range(universe.h):
    if universe.get(x, y) != ".":
      all_empty = False
      break
  if all_empty:
    universe.insertCol(x)

galaxies = []
for y in range(universe.h):
  for x in range(universe.w):
    if universe.get(x, y) == "#":
      galaxies.append(universe.getP(x, y))

score1 = 0
for i, a in enumerate(galaxies[:-1]):
  for b in galaxies[i+1:]:
    score1 += abs(a.x-b.x)+abs(a.y-b.y)



print_res("Part one:", score1, 1)
