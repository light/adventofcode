#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

ranges = []
ids = []

in_ranges = True
for l in inputs():
  if len(l) == 0:
    in_ranges = False
    continue
  if in_ranges:
    ranges.append([int(i) for i in l.split("-")])
  else:
    ids.append(int(l))


def in_any_range(id):
  for r in ranges:
    if id >= r[0] and id <= r[1]:
      return True
  return False

def count_fresh():
  n = 0
  for id in ids:
    if in_any_range(id):
      n += 1
  return n

print_res("Part one:", count_fresh(), 1)

