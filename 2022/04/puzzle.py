#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

def contains(a1,a2,b1,b2):
  return b1 >= a1 and b2 <= a2
def overlap(a1,a2,b1,b2):
  return b1 <= a2 and b2 >= a1

c1, c2 = 0, 0
for l in inputs():
  l.match('(\d+)-(\d+),(\d+)-(\d+)')
  a1, a2, b1, b2 = l.int(1), l.int(2), l.int(3), l.int(4)
  if contains(a1,a2,b1,b2) or contains(b1,b2,a1,a2):
    c1 += 1
  if overlap(a1,a2,b1,b2):
    c2 += 1

print_res("Part one:", c1, 1)
print_res("Part two:", c2, 2)
