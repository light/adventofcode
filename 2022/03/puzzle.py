#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

def p(c):
  v = ord(c)
  return v-64+26 if v < 97 else v-96
def common(*a):
  c = set.intersection(*[set(b) for b in a])
  return c.pop()

score1 = 0
score2 = 0
group = []
for l in inputs():
  a, b = l[:int(len(l)/2)], l[int(len(l)/2):]
  score1 += p(common(a, b))
  group.append(l)
  if len(group) == 3:
    score2 += p(common(group[0], group[1], group[2]))
    group = []

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
