#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *


inp = inputs()
a = next(inp)
b = next(inp)


races1 = list(zip([int(i) for i in a.split()[1:]], [int(i) for i in b.split()[1:]]))
races2 = [(int(a.split(":")[1].replace(" ", "")), int(b.split(":")[1].replace(" ", "")))]

def boat_distance(race_time, press_time):
  return (race_time-press_time)*press_time

def score1(races):
  score = 1
  for race in races:
    n = 0
    for press_time in range(race[0]):
      if boat_distance(race[0], press_time) > race[1]:
        n += 1
    score *= n
  return score


print_res("Part one:", score1(races1), 1)
print_res("Part two:", score1(races2), 2)
