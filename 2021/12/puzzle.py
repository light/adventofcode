#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
import sys

caves = {}
for l in sys.stdin:
  a, b = l.strip().split("-")
  caves.setdefault(a,[]).append(b)
  caves.setdefault(b,[]).append(a)

def allow_visit_one(path, b):
  return b.isupper() or not b in path

def allow_visit_two(path, b):
  if b.isupper() or not b in path:
    return True
  for c in caves:
    if c.islower() and path.count(c) >=2:
      return False
  return True

def branches(path, allow_visit):
  n = 0
  for b in caves[path[-1]]:
    if b == "end":
      n += 1
    elif b != "start" and allow_visit(path, b):
      n += branches(path + [b], allow_visit)
  return n

print_res("Part one:", branches(["start"], allow_visit_one), 1)
print_res("Part two:", branches(["start"], allow_visit_two), 2)
