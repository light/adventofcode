#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from board import Board, P

rolls = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    rolls.set(x, y, v)

def accessible_roll(x, y):
  p = rolls.getP(x, y)
  if p.val != "@":
    return False
  n = sum(1 if p.val == '@' else 0 for p in rolls.neighbors8(p))
  return n < 4

score1 = rolls.visit(lambda count, x, y, v: count+1 if accessible_roll(x, y) else count, 0)

print_res("Part one:", score1, 1)
