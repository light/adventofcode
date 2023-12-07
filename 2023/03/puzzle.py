#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

schematic = Board('.')
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    schematic.set(x, y, v)

numbers = []
number = None
for y in range(schematic.h):
  for x in range(schematic.w):
    c = schematic.get(x, y)
    if c.isdigit():
      if number is None:
        number = [x, y, 1]
        numbers.append(number)
      else:
        number[2] += 1
    elif number:
      number = None

def in_range(x, y):
  return x > 0 and x < schematic.w-1 and y > 0 and y < schematic.h-1

def neighbors(number):
  x, y, l = number[0], number[1], number[2]
  for j in [-1, 0, 1]:
    if in_range(x-1, y+j):
      yield [x-1, y+j]
    if in_range(x+l, y+j):
      yield [x+l, y+j]
  for i in range(l):
    if in_range(x+i, y-1):
      yield [x+i, y-1]
    if in_range(x+i, y+1):
      yield [x+i, y+1]

def getNum(number):
  n = ""
  for x in range(number[2]):
    n += schematic.get(number[0]+x, number[1])
  return int(n)

score1 = 0
for number in numbers:
  for n in neighbors(number):
    if schematic.get(n[0], n[1]) not in "0123456789.":
      score1 += getNum(number)
      break

print_res("Part one:", score1, 1)

score2 = 0
for y in range(schematic.h):
  for x in range(schematic.w):
    if schematic.get(x, y) == "*":
      touching_nums = [n for n in numbers if x >= n[0]-1 and x <= n[0]+n[2] and y >= n[1]-1 and y <= n[1]+1]
      if len(touching_nums) == 2:
        score2 += getNum(touching_nums[0]) * getNum(touching_nums[1])

print_res("Part two:", score2, 2)
