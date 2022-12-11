#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board

dirs = {"U": [0,1], "D": [0,-1], "R": [1,0], "L": [-1,0]}
rope = [0,0,0,0] # head xy, tail xy
map = Board('.')
map.set(rope[2], rope[3], '#')
def sgn(a, b): return 1 if a > b else -1 if a < b else 0
for l in inputs():
  l.match('(.) (\d+)')
  d = dirs[l.str(1)]
  for i in range(l.int(2)):
    rope[0] += d[0]; rope[1] += d[1]
    if abs(rope[0] - rope[2]) >= 2 or abs(rope[1] - rope[3]) >= 2:
      rope[2] += sgn(rope[0], rope[2])
      rope[3] += sgn(rope[1], rope[3])
    map.set(rope[2], rope[3], '#')

visited = map.visit(lambda count, x, y, v: count+1 if v == "#" else count, 0)

print_res("Part one:", visited, 1)
