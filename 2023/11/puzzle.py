#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P
from path import a_star

universe = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    universe.set(x, y, v)

empty_rows = []
empty_cols = []
for y in range(universe.h):
  all_empty = True
  for x in range(universe.w):
    if universe.get(x, y) != ".":
      all_empty = False
      break
  if all_empty:
    empty_rows.append(y)
for x in range(universe.w):
  all_empty = True
  for y in range(universe.h):
    if universe.get(x, y) != ".":
      all_empty = False
      break
  if all_empty:
    empty_cols.append(x)

galaxies = []
for y in range(universe.h):
  for x in range(universe.w):
    if universe.get(x, y) == "#":
      galaxies.append(universe.getP(x, y))


# Return index of val in sorted list
def index_in_list(list, val):
  for i, v in enumerate(list):
    if val < v:
      return i
  return len(list)
def distance(a, b, empty_factor):
  num_empty_rows = index_in_list(empty_rows, a.y) - index_in_list(empty_rows, b.y)
  num_empty_cols = index_in_list(empty_cols, a.x) - index_in_list(empty_cols, b.x)
  return abs(a.x-b.x)+abs(a.y-b.y)+(abs(num_empty_rows)+abs(num_empty_cols))*(empty_factor-1)

def sum_distances(galaxies, empty_factor):
  dist = 0
  for i, a in enumerate(galaxies[:-1]):
    for b in galaxies[i+1:]:
      dist += distance(a, b, empty_factor)
  return dist

score1 = sum_distances(galaxies, 2)
score2 = sum_distances(galaxies, int(cmdline_arg(1)))


print_res("Part one:", score1, 2)
print_res("Part two:", score2, 3)
