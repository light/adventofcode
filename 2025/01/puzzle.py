#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

pos = 50
score1 = 0

for step in inputs():
  n = int(step[1:])
  if step[0] == "L":
    pos = (pos-n) % 100
  else:
    pos = (pos+n) % 100
  if pos == 0:
    score1 += 1

print_res("Part one:", score1, 1)
