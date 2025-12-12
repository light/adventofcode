#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *


score1 = 0

for r in next(inputs()).split(","):
  a, b = [int(i) for i in r.split("-")]
  for i in range(a, b + 1):
    id = str(i)
    if len(id) % 2 == 0:
      m = len(id) // 2
      if id[:m] == id[m:]:
        score1 += int(id)

print_res("Part one:", score1, 1)