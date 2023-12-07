#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

seeds = []
maps = []

inp = inputs()
l = next(inp)
l.match(r"seeds: (.*)")
seeds = [int(i) for i in l.str(1).split()]

map = None
for l in inp:
  if not l and map is not None:
    maps.append(map)
    map = None
  elif l and map is None:
    map = []
  elif l:
    l.match(r"(\d+) (\d+) (\d+)")
    map.append([l.int(2), l.int(1), l.int(3)])
maps.append(map)

def get_matching_range(map, seed):
    for range in map:
      if seed >= range[0] and seed <= range[0]+range[2]:
        return range

def map_all(seed):
  for map in maps:
    range = get_matching_range(map, seed)
    if range:
      seed = range[1] + seed-range[0]
  return seed


score1 = min([map_all(seed) for seed in seeds])

print_res("Part one:", score1, 1)
