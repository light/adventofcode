#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

map = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    map.set(x, y, v)


def dance_of_the_sea_cucumbers(map):
  target = Board('.')
  target.extend(map.w, map.h)
  for y in range(map.h):
    for x in range(map.w):
      c = map.get(x, y)
      if c == ">":
        right = (x+1) % map.w
        if map.get(right, y) == ".":
          target.set(right, y, c)
        else:
          target.set(x, y, c)
  for y in range(map.h):
    for x in range(map.w):
      c = map.get(x, y)
      if c == "v":
        down = (y+1) % map.h
        if map.get(x, down) != "v" and target.get(x, down) == '.':
          target.set(x, down, c)
        else:
          target.set(x, y, c)
  return target

prev_map = None; i = 0
while map != prev_map:
  prev_map = map
  map = dance_of_the_sea_cucumbers(prev_map)
  i += 1

print_res("Part one:", i, 1)
