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

for l in inputs():
  l.match('move (\d+) from (\d+) to (\d+)')
  for i in range(l.int(1)):
    stacks[l.int(3)-1].append(stacks[l.int(2)-1].pop())

tops = "".join([s.pop() for s in stacks])

print_res("Part one:", tops, 1)
