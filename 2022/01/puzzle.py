#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

elves = []
c = 0
for l in inputs():
  if len(l) == 0:
    elves.append(c)
    c = 0
  else:
    c += int(l)
elves.append(c)

print_res("Part one:", max(elves), 1)

top3 = sum(sorted(elves)[-3:])

print_res("Part two:", top3, 2)
