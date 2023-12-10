#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

inp = inputs()
a = next(inp).split()[1:]
b = next(inp).split()[1:]

races = list(zip([int(i) for i in a], [int(i) for i in b]))

def boat_distance(race_time, press_time):
  return (race_time-press_time)*press_time


def score(races):
  score = 1
  for race in races:
    n = 0
    for press_time in range(race[0]):
      if boat_distance(race[0], press_time) > race[1]:
        n += 1
    score *= n
  return score


print_res("Part one:", score(races), 1)
