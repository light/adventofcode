#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P

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

def diff_idx(a, b):
  return [i for i, z in enumerate(zip(a, b)) if z[0] != z[1]]

# Check vertical mirror with `left` columns immediately to the left of reflection line
def check_vertical_diff(scan, left):
  diff = []
  for x in range(min(left, scan.w-left)):
    diff += [(left-x-1, y) for y in diff_idx(scan.getCol(left-x-1), scan.getCol(left+x))]
  return diff

# Check horizontal mirror with `top` rows immediately above the reflection line
def check_horizontal_diff(scan, top):
  diff = []
  for y in range(min(top, scan.h-top)):
    diff += [(x, top-y-1) for x in diff_idx(scan.getRow(top-y-1), scan.getRow(top+y))]
  return diff

# Look for reflections with a certain number of smudges
def check_reflection_smudges(scan, wanted_smudges = 0):
  for y in range(1, scan.h):
    diff = check_horizontal_diff(scan, y)
    if len(diff) == wanted_smudges:
      return y * 100
  for x in range(1, scan.w):
    diff = check_vertical_diff(scan, x)
    if len(diff) == wanted_smudges:
      return x

score1 = 0
score2 = 0
for scan in scans:
  score1 += check_reflection_smudges(scan)
  score2 += check_reflection_smudges(scan, 1)

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
