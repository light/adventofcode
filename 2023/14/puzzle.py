#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P

rocks = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    rocks.set(x, y, v)

def roll_top(rocks):
  moved = True
  tmp = rocks.copy()
  while moved:
    moved = False
    for y in range(1, rocks.h):
      for x in range(rocks.w):
        if tmp.get(x, y) == "O" and tmp.get(x, y-1) == ".":
          tmp.set(x, y, "."); tmp.set(x, y-1, "O")
          moved = True
  return tmp

rocks = roll_top(rocks)

score1 = rocks.visit(lambda acc, x, y, v: acc+rocks.h-y if v == "O" else acc, 0)

print_res("Part one:", score1, 1)