#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
from board import Board, P
from queue import PriorityQueue

map = Board()
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    map.set(x, y, int(v))


# (Almost) straight from https://en.wikipedia.org/wiki/A*_search_algorithm
# and https://www.redblobgames.com/pathfinding/a-star/implementation.html
def reconstruct_path(cameFrom, current):
  total_path = [current]
  while current in cameFrom:
    current = cameFrom[current]
    total_path.append(current)
  return list(reversed(total_path))
def heuristic(p1, p2):
  # Best case all 1 cost in a straight line
  return abs(p1.x-p2.x) + abs(p1.y-p2.y)
def a_star(start, goal, h):
  frontier = PriorityQueue()
  frontier.put((0, start))
  came_from = {}

  cost_so_far = {}
  cost_so_far[start] = 0

  while not frontier.empty():
    current = frontier.get()[1]
    if current == goal:
      return reconstruct_path(came_from, current)

    for neighbor in map.neighbors4(current):
      new_score = cost_so_far[current] + map.get(neighbor.x, neighbor.y)
      if not neighbor in cost_so_far or new_score < cost_so_far[neighbor]:
        came_from[neighbor] = current
        cost_so_far[neighbor] = new_score
        prio = new_score + h(neighbor, goal)
        frontier.put((prio, neighbor))

  # No nodes left to consider but goal was never reached
  return None

def score(path):
  return sum([map.get(n.x, n.y) for n in path[1:]])

path = a_star(P(0,0), P(map.w-1, map.h-1), heuristic)
print_res("Part one", score(path), 1)

w = map.w; h = map.h
def wrap(v): return 1 if v == 10 else v
for i in range(w*4):
  for j in range(map.h):
    map.set(w+i, j, wrap(map.get(i, j)+1))
for j in range(h*4):
  for i in range(map.w):
    map.set(i, h+j, wrap(map.get(i, j)+1))

path = a_star(P(0,0), P(map.w-1, map.h-1), heuristic)
print_res("Part two", score(path), 2)
