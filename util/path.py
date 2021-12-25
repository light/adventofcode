#!/usr/bin/env python3

from queue import PriorityQueue

# Generalized A* pathfinding
# Largely from https://en.wikipedia.org/wiki/A*_search_algorithm
# and https://www.redblobgames.com/pathfinding/a-star/implementation.html
def a_star(start, neighbors_with_cost, goal_condition, heuristic):
  frontier = PriorityQueue()
  frontier.put((0, start))
  came_from = {}

  cost_so_far = {}
  cost_so_far[start] = 0

  while not frontier.empty():
    current = frontier.get()[1]
    if goal_condition(current):
      return reconstruct_path(came_from, current)

    for neighbor, cost in neighbors_with_cost(current):
      new_score = cost_so_far[current] + cost
      if not neighbor in cost_so_far or new_score < cost_so_far[neighbor]:
        came_from[neighbor] = (current, cost)
        cost_so_far[neighbor] = new_score
        prio = new_score + heuristic(neighbor)
        frontier.put((prio, neighbor))

  # No nodes left to consider but goal was never reached
  return None, None

def reconstruct_path(cameFrom, current):
  total_path = [current]
  total_cost = 0
  while current in cameFrom:
    current, cost = cameFrom[current]
    total_path.append(current)
    total_cost += cost
  return list(reversed(total_path)), total_cost
