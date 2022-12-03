#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

def p(c):
  v = ord(c)
  return v-64+26 if v < 97 else v-96
def common(a, b):
  c = set(a).intersection(set(b))
  return c.pop()

s = 0
for l in inputs():
  a, b = l[:int(len(l)/2)], l[int(len(l)/2):]
  s += p(common(a, b))

print_res("Part one:", s, 1)