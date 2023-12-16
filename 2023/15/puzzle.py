#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from functools import reduce
from collections import OrderedDict


steps = next(inputs()).split(",")

def hash(s):
  return reduce(lambda h, c: ((h+ord(c))*17)%256, s, 0)

score1 = sum([hash(s) for s in steps])

print_res("Part one:", score1, 1)


boxes = [OrderedDict() for i in range(256)]
for step in steps:
  op_add = step[-2] == "="
  label = step[0:-2] if op_add else step[0:-1]
  h = hash(label)
  if op_add:
    boxes[h][label] = int(step[-1])
  else:
    if label in boxes[h]:
      del boxes[h][label]
score2 = 0
for i, box in enumerate(boxes):
  if box:
    for j, (k, v) in enumerate(box.items()):
      score2 += (i+1) * (j+1) * v

print_res("Part two:", score2, 2)
