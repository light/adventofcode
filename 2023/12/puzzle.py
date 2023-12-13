#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from math import factorial
from tqdm import tqdm
import os

springs = []
for l in inputs():
  a, b = l.split()
  springs.append((a, [int(i) for i in b.split(",")]))

cache_file = {}
for l in input_file("cache.txt"):
  a, b, c = l.split()
  cache_file[(a, b)] = int(c)
def save_cache():
  with open("cache.txt.tmp", "w") as f:
    for k, v in cache_file.items():
      f.write(f"{k[0]} {k[1]} {v}\n")
  os.rename("cache.txt.tmp", "cache.txt")

def for_each_slot(n_slots, max_id, apply, s=None, offset=0, add=0):
  if n_slots > max_id:
    return
  if offset == 0:
    s = [0]*n_slots
  for i in range(max_id-n_slots+1):
    s[offset] = i+offset+add
    if n_slots == 1:
      apply(s)
    else:
      for_each_slot(n_slots-1, max_id-i-1, apply, s, offset=offset+1, add=add+i)

def for_each_possibility(springs, n_total, apply_possible_slots):
  idx_slot = [i for i, c in enumerate(springs) if c == "?"]
  n_slots = n_total-springs.count("#")
  springs = springs.replace("?", ".")
  if n_slots == 0:
    apply_possible_slots(springs, idx_slot, [])
  else:
    max_id = len(idx_slot)
    N = int(factorial(max_id)/(factorial(n_slots)*factorial(max_id-n_slots)))
    print("N to check =", N)
    progress = tqdm(total=N)
    n = 0
    def apply_progress(*args):
      apply_possible_slots(*args)
      nonlocal n
      n += 1
      if n%1000 == 0:
        progress.update(1000)
    for_each_slot(n_slots, max_id, lambda slots: apply_progress(springs, idx_slot, slots))
    progress.close()

def count_valid_possibilities(springs, counts):
  key = (springs, ",".join(map(str, counts)))
  if key in cache_file:
    print("Load from cache", cache_file[key])
    return cache_file[key]
  tmp_springs = [1 if s == "#" else 0 for s in springs]
  tmp_pos = [0]*len(springs)
  ok = 0
  def apply_possible_slots(s, idx_slot, possible_slots):
    nonlocal ok
    for s in possible_slots:
        tmp_pos[idx_slot[s]] = 1
    l = len(tmp_springs)
    j = 0
    for i in range(len(counts)):
      while j < l and (tmp_springs[j] == 0 and tmp_pos[j] == 0):
        j += 1
      c = 0
      while j < l and (tmp_springs[j] == 1 or tmp_pos[j] == 1):
        j += 1
        c += 1
      if c != counts[i]:
        break
      elif i == len(counts)-1:
        ok += 1
    for s in possible_slots:
        tmp_pos[idx_slot[s]] = 0
  for_each_possibility(springs, sum(counts), apply_possible_slots)
  print("Result", ok)
  cache_file[key] = ok
  save_cache()
  return ok


score1 = 0
for spring in springs:
  score1 += count_valid_possibilities(*spring)

print_res("Part one:", score1, 1)

score2 = 0
nb_repeat = 5
for i, spring in enumerate(springs):
  print(i, spring)
  score2 += count_valid_possibilities("?".join([spring[0]]*nb_repeat), spring[1]*nb_repeat)

print_res("Part two:", score2, 2)