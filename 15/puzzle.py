#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
from board import Board, P
from path import a_star

map = Board()
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    map.set(x, y, int(v))

goal = P(map.w-1, map.h-1)
def neighbors(p):
  return [(n, map.get(n.x, n.y)) for n in map.neighbors4(p)]
def goal_reached(p):
  return p == goal
def heuristic(p):
  # Best case all 1 cost in a straight line
  return abs(goal.x-p.x) + abs(goal.y-p.y)

def score(path):
  return sum([map.get(n.x, n.y) for n in path[1:]])

path, total_cost = a_star(P(0,0), neighbors, goal_reached, heuristic)
print_res("Part one", score(path), 1)

w = map.w; h = map.h
def wrap(v): return 1 if v == 10 else v
for i in range(w*4):
  for j in range(map.h):
    map.set(w+i, j, wrap(map.get(i, j)+1))
for j in range(h*4):
  for i in range(map.w):
    map.set(i, h+j, wrap(map.get(i, j)+1))

goal = P(map.w-1, map.h-1)
path, total_cost = a_star(P(0,0), neighbors, goal_reached, heuristic)
print_res("Part two", score(path), 2)
