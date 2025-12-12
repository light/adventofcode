#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from geom import Segment

ranges = []
ids = []

in_ranges = True
for l in inputs():
  if len(l) == 0:
    in_ranges = False
    continue
  if in_ranges:
    ranges.append(Segment(*[int(i) for i in l.split("-")]))
  else:
    ids.append(int(l))


def in_any_range(id):
  for r in ranges:
    if r.is_inside(id):
      return True
  return False

def count_fresh():
  n = 0
  for id in ids:
    if in_any_range(id):
      n += 1
  return n

print_res("Part one:", count_fresh(), 1)


min_range = min(r.x1 for r in ranges)
max_range = max(r.x2 for r in ranges)

spoiled_ranges = [Segment(min_range, max_range)]
for r in ranges:
  new_ranges = []
  for s in spoiled_ranges:
    new_ranges.extend(s.sub(r))
  spoiled_ranges = new_ranges

score2 = (max_range-min_range+1) - sum(s.length() for s in spoiled_ranges)

print_res("Part two:", score2, 2)
