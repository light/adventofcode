#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *


score1 = 0
score2 = 0

for r in next(inputs()).split(","):
  a, b = [int(i) for i in r.split("-")]
  for i in range(a, b + 1):
    id = str(i)
    l = len(id)
    for d in range(2, l+1):
      if l % d == 0:
        m = l // d
        equals = True
        for k in range(1, d):
          if id[:m] != id[m*k:m*(k+1)]:
            equals = False
            break
        if equals:
          if d == 2:
            score1 += int(id)
          score2 += int(id)
          break

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
