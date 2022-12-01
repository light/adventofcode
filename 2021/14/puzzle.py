#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
import sys
import functools

seed = None
rules = {}
for l in inputs():
  if l.match('(.{2}) -> (.)'):
    rules[l.str(1)] = l.str(2)
  elif l:
    seed = l

def addv(a, k, v): a[k] = a.get(k, 0) + v
def add_counts(a, b):
  for k, v in b.items():
    addv(a, k, v)
@functools.cache
def count_elements(seed, steps):
  counts = {}
  if steps == 0:
    for e in seed:
      addv(counts, e, 1)
  else:
    for i in range(len(seed)-1):
      part = seed[i] + rules[seed[i:i+2]] + seed[i+1]
      add_counts(counts, count_elements(part, steps-1))
      # Don't count twice where parts join together
      if i != 0:
        addv(counts, part[0], -1)
  return counts

def score(counts):
  maxe = max(counts, key=counts.get)
  mine = min(counts, key=counts.get)
  return counts[maxe] - counts[mine]

print_res("Part one:", score(count_elements(seed, 10)), 1)
print_res("Part two:", score(count_elements(seed, 40)), 2)
