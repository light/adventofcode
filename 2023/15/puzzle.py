#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from functools import reduce

steps = next(inputs()).split(",")

def hash(s):
  return reduce(lambda h, c: ((h+ord(c))*17)%256, s, 0)

score1 = sum([hash(s) for s in steps])

print_res("Part one:", score1, 1)
