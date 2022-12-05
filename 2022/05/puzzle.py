#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *


stacks = DynArray(lambda: [])
for l in inputs():
  if "[" in l:
    for i in range(int(len(l)/4+1)):
      c = l[i*4+1:i*4+1+1]
      if c != " ":
        stacks[i].insert(0, c)
  if len(l) == 0:
    break

stacks2 = stacks.copy()
for l in inputs():
  l.match('move (\d+) from (\d+) to (\d+)')
  n = l.int(1)
  for i in range(n):
    stacks[l.int(3)-1].append(stacks[l.int(2)-1].pop())
    stacks2[l.int(3)-1].append(stacks2[l.int(2)-1].pop(len(stacks2[l.int(2)-1])-n+i))

def tops(stacks):
  return "".join([s[-1] for s in stacks])

print_res("Part one:", tops(stacks), 1)
print_res("Part two:", tops(stacks2), 2)
