#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from board import Board, P
from typing import NamedTuple

class SeedRange(NamedTuple):
  idx_start: int
  idx_end: int

class MapRange(NamedTuple):
  from_idx_start: int
  from_idx_end: int
  to_idx: int

seeds1 = []
seeds2 = []
maps = []

inp = inputs()
l = next(inp)
l.match(r"seeds: (.*)")
seeds = l.str(1).split()
for i in range(len(seeds)):
  seeds1.append(SeedRange(int(seeds[i]), int(seeds[i])))
for i in range(0, len(seeds), 2):
  seeds2.append(SeedRange(int(seeds[i]), int(seeds[i])+int(seeds[i+1])-1))

map = None
for l in inp:
  if not l and map is not None:
    maps.append(map)
    map = None
  elif l and map is None:
    map = []
  elif l:
    l.match(r"(\d+) (\d+) (\d+)")
    map.append(MapRange(from_idx_start=l.int(2), to_idx=l.int(1), from_idx_end=l.int(2)+l.int(3)-1))
maps.append(map)
maps = [sorted(map, key=lambda x: x.from_idx_start) for map in maps]


def map_value(map_range, value):
  if value >= map_range.from_idx_start and value <= map_range.from_idx_end:
    return value + map_range.to_idx - map_range.from_idx_start
  raise "Value out of MapRange"

def map_ranges(map, seed_ranges):
  mapped_ranges = []
  for map_range in map:
    unmapped_ranges = []
    for seed_range in seed_ranges:
      a1, a2 = seed_range.idx_start, seed_range.idx_end
      b1, b2 = map_range.from_idx_start, map_range.from_idx_end
      if b1 <= a1 and b2 >= a1 and b2 < a2:
        mapped_ranges.append(SeedRange(map_value(map_range, a1), map_value(map_range, b2)))
        unmapped_ranges.append(SeedRange(b2+1, a2))
      elif b1 > a1 and b1 <= a2 and b2 >= a2:
        unmapped_ranges.append(SeedRange(a1, b1-1))
        mapped_ranges.append(SeedRange(map_value(map_range, b1), map_value(map_range, a2)))
      elif b1 > a1 and b2 < a2:
        unmapped_ranges.append(SeedRange(a1, b1-1))
        mapped_ranges.append(SeedRange(map_value(map_range, b1), map_value(map_range, b2)))
        unmapped_ranges.append(SeedRange(b2+1, a2));
      elif b1 <= a1 and b2 >= a2:
        mapped_ranges.append(SeedRange(map_value(map_range, a1), map_value(map_range, a2)))
      else:
        unmapped_ranges.append(seed_range)
    seed_ranges = unmapped_ranges
  return mapped_ranges + seed_ranges

def map_all(seed_ranges):
  target_ranges = []
  for seed_range in seed_ranges:
    sss = [seed_range]
    for map in maps:
      sss = map_ranges(map, sss)
    target_ranges += sss
  return target_ranges

def score(seed_ranges):
  return min([seed_range.idx_start for seed_range in seed_ranges])


print_res("Part one:", score(map_all(seeds1)), 1)
print_res("Part two:", score(map_all(seeds2)), 2)
