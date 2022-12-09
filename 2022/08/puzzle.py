#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board

trees = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    trees.set(x, y, int(v))

vis = Board(lambda: [-1,-1,-1,-1]) # top, down, left, right
vis.extend(trees.w, trees.h)
for y in range(trees.h):
  maxLeft = maxRight = -1
  for x in range(trees.w):
    h = trees.get(x, y)
    v = vis.get(x, y)
    v[2] = maxLeft
    maxLeft = max(maxLeft, h)
    h = trees.get(trees.w-x-1, y)
    v = vis.get(trees.w-x-1, y)
    v[3] = maxRight
    maxRight = max(maxRight, h)
for x in range(trees.w):
  maxTop = maxDown = -1
  for y in range(trees.h):
    h = trees.get(x, y)
    v = vis.get(x, y)
    v[0] = maxTop
    maxTop = max(maxTop, h)
    h = trees.get(x, trees.h-y-1)
    v = vis.get(x, trees.h-y-1)
    v[1] = maxDown
    maxDown = max(maxDown, h)

n_visibles = 0
for y in range(trees.h):
  for x in range(trees.w):
    h = trees.get(x, y)
    v = vis.get(x, y)
    if h > v[0] or h > v[1] or h > v[2] or h > v[3]:
      n_visibles += 1


print_res("Part one:", n_visibles, 1)
