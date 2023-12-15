#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P
from path import a_star

scans = []
y = 0; scan = None
for l in inputs():
  if len(l) == 0:
    y = 0; scan = None
    continue
  if scan is None:
    scan = Board('.')
    scans.append(scan)
  for x, v in enumerate(l):
    scan.set(x, y, v)
  y += 1

# Check vertical mirror with `left` columns immediately to the left of reflection line
def check_vertical(scan, left):
  for x in range(min(left, scan.w-left)):
    if scan.getCol(left-x-1) != scan.getCol(left+x):
      return False
  return True

# Check horizontal mirror with `top` columns immediately above the reflection line
def check_horizontal(scan, top):
  for y in range(min(top, scan.h-top)):
    if scan.getRow(top-y-1) != scan.getRow(top+y):
      return False
  return True

def check_reflection(scan):
  for x in range(1, scan.w):
    if check_vertical(scan, x):
      return x
  for y in range(1, scan.h):
    if check_horizontal(scan, y):
      return y * 100


score1 = 0
for scan in scans:
  score1 += check_reflection(scan)

print_res("Part one:", score1, 1)
