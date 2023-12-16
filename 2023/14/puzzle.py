#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P

rocks = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    rocks.set(x, y, v)

def roll_in_direction(rocks, dx, dy):
  moved = True
  tmp = rocks.copy()
  while moved:
    moved = False
    for y in range(rocks.h):
      for x in range(rocks.w):
        if tmp.is_inside(x+dx, y+dy) and tmp.get(x, y) == "O" and tmp.get(x+dx, y+dy) == ".":
          tmp.set(x, y, "."); tmp.set(x+dx, y+dy, "O")
          moved = True
  return tmp

def roll_top(rocks):
  return roll_in_direction(rocks, 0, -1)

def calculate_load(rocks):
  return rocks.visit(lambda acc, x, y, v: acc+rocks.h-y if v == "O" else acc, 0)

score1 = calculate_load(roll_top(rocks))
print_res("Part one:", score1, 1)


def spin_cycle(rocks):
  rocks = roll_in_direction(rocks, 0, -1)
  rocks = roll_in_direction(rocks, -1, 0)
  rocks = roll_in_direction(rocks, 0, 1)
  rocks = roll_in_direction(rocks, 1, 0)
  return rocks

def find_period(rocks):
  previous = []
  while True:
    previous.append(rocks)
    rocks = spin_cycle(rocks)
    for i, prev in enumerate(previous):
      if rocks == prev:
        return (i, len(previous)-i, rocks)

n_cycles = 1000000000
phase, period, rocks = find_period(rocks)
remainder = (n_cycles - phase) % period
for i in range(remainder):
  rocks = spin_cycle(rocks)
score2 = calculate_load(rocks)

print_res("Part two:", score2, 2)
