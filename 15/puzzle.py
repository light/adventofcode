#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
from board import Board, P
from heapq import heappush, heappop

map = Board()
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    map.set(x, y, int(v))

# Straight from https://en.wikipedia.org/wiki/A*_search_algorithm
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
  openSet = set()
  openSet.add(start)
  cameFrom = {}

  # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
  gScore = {} # map with default value of Infinity
  gScore[start] = 0

  # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
  # how short a path from start to finish can be if it goes through n.
  fScore = {} # map with default value of Infinity
  fScore[start] = h(start, goal)

  while openSet:
    # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
    current = min(openSet, key=lambda n: fScore[n]) # the node in openSet having the lowest fScore[] value
    if current == goal:
      return reconstruct_path(cameFrom, current)

    openSet.remove(current)
    for neighbor in map.neighbors4(current):
      # d(current,neighbor) is the weight of the edge from current to neighbor
      # tentative_gScore is the distance from start to the neighbor through current
      tentative_gScore = gScore[current] + map.get(neighbor.x, neighbor.y)
      if not neighbor in gScore or tentative_gScore < gScore[neighbor]:
        # This path to neighbor is better than any previous one. Record it!
        cameFrom[neighbor] = current
        gScore[neighbor] = tentative_gScore
        fScore[neighbor] = tentative_gScore + h(neighbor, goal)
        if not neighbor in openSet:
          openSet.add(neighbor)

  # Open set is empty but goal was never reached
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
