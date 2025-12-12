#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from board import Board, P

rolls = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    rolls.set(x, y, v)

def is_accessible_roll(x, y):
  p = rolls.getP(x, y)
  if p.val != "@":
    return False
  n = sum(1 if p.val == '@' else 0 for p in rolls.neighbors8(p))
  return n < 4

def remove_accessible_rolls(rolls):
  accessible_rolls = rolls.visit(lambda acc, x, y, v: acc+[P(x,y)] if is_accessible_roll(x, y) else acc, [])
  for p in accessible_rolls:
    rolls.set(p.x, p.y, ".")
  return len(accessible_rolls)

def remove_all_accessible_rolls(rolls):
  sum = 0
  while True:
    n = remove_accessible_rolls(rolls)
    if n == 0:
      break
    sum += n
  return sum

score1 = remove_accessible_rolls(rolls.copy())
score2 = remove_all_accessible_rolls(rolls)

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
