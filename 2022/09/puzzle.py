#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board

dirs = {"U": [0,1], "D": [0,-1], "R": [1,0], "L": [-1,0]}
steps = [l for l in inputs()]

def sgn(a, b): return 1 if a > b else -1 if a < b else 0
def simulate_rope(steps, knots):
  rope = [[0,0] for i in range(knots)] # knots xy
  map = Board('.')
  map.set(0, 0, '#')
  for s in steps:
    s.match('(.) (\d+)')
    d = dirs[s.str(1)]
    for i in range(s.int(2)):
      knot = rope[0]
      knot[0] += d[0]; knot[1] += d[1]
      for k in range(1, len(rope)):
        knotA, knotB = rope[k-1], rope[k]
        if abs(knotA[0] - knotB[0]) >= 2 or abs(knotA[1] - knotB[1]) >= 2:
          knotB[0] += sgn(knotA[0], knotB[0])
          knotB[1] += sgn(knotA[1], knotB[1])
      tail = rope[-1]
      map.set(tail[0], tail[1], '#')
  return map

def visited(steps, knots):
  map = simulate_rope(steps, knots)
  return map.visit(lambda count, x, y, v: count+1 if v == "#" else count, 0)

print_res("Part one:", visited(steps, 2), 1)
print_res("Part one:", visited(steps, 10), 2)
