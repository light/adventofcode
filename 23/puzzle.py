#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
from collections import namedtuple
from path import a_star
from board import Board

P = namedtuple("P", ["x", "y"])

pos = [[] for i in range(4)]
l = list(inputs())
for i in range(len(l)):
  for j in range(len(l[i])):
    if l[i][j] in "ABCD":
      pos[ord(l[i][j]) - 65].append(P(j, i))
pos = tuple(sum(pos, []))

def occupied(pos, P, ignore_idx):
  for i, p in enumerate(pos):
#    if i != ignore_idx and p == P:
    if p == P:
      return True
  return False
def occupied_by(pos, P):
  for i, p in enumerate(pos):
    if p == P:
      return i
  return None
def target(i):
  return i // 2 * 2 + 3
# Checks if a pod can move laterally to tx position
def can_shift_to(pos, p, tx):
    x = p.x
    if x < tx:
      while x < 12:
        if x == tx-1:
          return True
        x += 2 if x >= 2 else 1
        if occupied(pos, P(x, 1), i):
          return False
    else:
      while x > 0:
        if x == tx+1:
          return True
        x -= 2 if x <= 10 else 1
        if occupied(pos, P(x, 1), i):
          return False
# Returns whether no unwanted pods are at tx
def no_interloper_at_target(pos, tx):
  for i, p in enumerate(pos):
    if target(i) != tx and p.x == tx:
      return False
  return True
def valid_moves(pos, i):
  res = []
  p = pos[i]
  tx = target(i)
  if p.x == tx and no_interloper_at_target(pos, tx):
    pass # Don't move if already in place
  elif p.y == 2 or (p.y == 3 and not occupied(pos, P(p.x, p.y-1), i)):
    x = p.x-1
    while x > 0 and not occupied(pos, P(x, 1), i):
      res.append(P(x, 1))
      x -= 2 if x > 2 else 1
    x = p.x+1
    while x < 12 and not occupied(pos, P(x, 1), i):
      res.append(P(x, 1))
      x += 2 if x < 10 else 1
  elif p.y == 1:
    if can_shift_to(pos, p, tx) and no_interloper_at_target(pos, tx):
      y = 3
      while occupied(pos, P(tx, y), i):
        y -= 1
      res.append(P(tx, y))
  return res

def move_cost(p1, p2, i):
  c = [1, 1, 10, 10, 100, 100, 1000, 1000]
  return c[i]*(abs(p2.x-p1.x)+abs(p2.y-p1.y))
def next_states(pos):
  next_pos = []
  for i, p in enumerate(pos):
    for move in valid_moves(pos, i):
      next_pos.append((pos[:i]+(move,)+pos[i+1:], move_cost(p, move, i)))
  return next_pos
def goal_reached(pos):
  for i, p in enumerate(pos):
    if p.x != target(i):
      return False
  return True
def heuristic(p):
  return 0

def print_state(pos):
  b = Board(" ")
  with open("input_test") as f:
    for y, l in enumerate(f.readlines()):
      for x, v in enumerate(l.rstrip()):
        b.set(x, y, "." if v in "ABCD" else v)
  for i, p in enumerate(pos):
    b.set(p.x, p.y, chr(i//2 + 65))
  b.print()



path, total_cost = a_star(pos, next_states, goal_reached, heuristic)

print_res("Part one", total_cost, 1)
