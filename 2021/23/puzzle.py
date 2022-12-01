#!/usr/bin/env -S PYTHONPATH=../../util python3

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
N = len(pos) // 4

def occupied(pos, P):
  for i, p in enumerate(pos):
    if p == P:
      return True
  return False
def occupied_by(pos, P):
  for i, p in enumerate(pos):
    if p == P:
      return i
  return None
def target(i):
  return i // N * 2 + 3
# Checks if a pod can move laterally to tx position
def can_shift_to(pos, p, tx):
    x = p.x
    if x < tx:
      while x < 12:
        if x == tx-1:
          return True
        x += 2 if x >= 2 else 1
        if occupied(pos, P(x, 1)):
          return False
    else:
      while x > 0:
        if x == tx+1:
          return True
        x -= 2 if x <= 10 else 1
        if occupied(pos, P(x, 1)):
          return False
# Returns whether no unwanted pods are at tx
def no_interloper_at_target(pos, tx):
  for i, p in enumerate(pos):
    if target(i) != tx and p.x == tx:
      return False
  return True
def free_to_move_out(pos, p):
  y = p.y
  while y != 2:
    y -= 1
    if  occupied(pos, P(p.x, y)):
      return False
  return True
def valid_moves(pos, i):
  res = []
  p = pos[i]
  tx = target(i)
  if p.x == tx and no_interloper_at_target(pos, tx):
    pass # Don't move if already in place
  elif p.y >= 2 and free_to_move_out(pos, p):
    x = p.x-1
    while x > 0 and not occupied(pos, P(x, 1)):
      res.append(P(x, 1))
      x -= 2 if x > 2 else 1
    x = p.x+1
    while x < 12 and not occupied(pos, P(x, 1)):
      res.append(P(x, 1))
      x += 2 if x < 10 else 1
  elif p.y == 1:
    if can_shift_to(pos, p, tx) and no_interloper_at_target(pos, tx):
      y = 1 + N
      while occupied(pos, P(tx, y)):
        y -= 1
      res.append(P(tx, y))
  return res

def move_cost(p1, p2, i):
  c = [1, 10, 100, 1000]
  return c[i // N]*(abs(p2.x-p1.x)+abs(p2.y-p1.y))
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

path, total_cost = a_star(pos, next_states, goal_reached, heuristic)

print_res("Part one" if N == 2 else "Part two", total_cost, 1)
