#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *


springs = []
for l in inputs():
  a, b = l.split()
  springs.append((a, [int(i) for i in b.split(",")]))


def list_slots(n_slots, max_id):
  if n_slots > max_id:
    return
  idx_slot = [0]*n_slots
  for i in range(max_id-n_slots+1):
    if n_slots == 1:
      yield [i]
    else:
      for s in list_slots(n_slots-1, max_id-i-1):
        yield [i] + [i+j+1 for j in s]

def list_all_possibilities(springs, n_total):
  idx_slot = [i for i, c in enumerate(springs) if c == "?"]
  n_slot = n_total-springs.count("#")
  springs = springs.replace("?", ".")
  if n_slot == 0:
    yield springs
  else:
    for slots in list_slots(n_slot, len(idx_slot)):
      tmp_springs = list(springs)
      for s in slots:
        tmp_springs[idx_slot[s]] = "#"
      yield "".join(tmp_springs)

def count_valid_possibilities(springs, counts):
  ok = 0
  for possibility in list_all_possibilities(springs, sum(counts)):
    try_counts = [len(group) for group in possibility.split(".") if group]
    if try_counts == counts:
      ok += 1
  return ok


score1 = 0
for spring in springs:
  score1 += count_valid_possibilities(*spring)

print_res("Part one:", score1, 1)
