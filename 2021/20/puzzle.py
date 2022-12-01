#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board

image = Board(".")
rule = next(inputs())
next(inputs())
for y, l in enumerate(inputs()):
  for x, c in enumerate(list(l)):
    image.set(x, y, c)
def code(img, x, y):
  code = 0
  for j in range(-1, 2):
    for i in range(-1, 2):
      code <<= 1
      if (x+i<0 or x+i>=img.w or y+j<0 or y+j>=img.h) and img.ø == "#":
        code += 1
      if x+i>=0 and x+i<img.w and y+j>=0 and y+j<img.h and img.get(x+i, y+j) == "#":
        code += 1
  return code
def enhance(image):
  res = image.copy()
  if rule[0] == "#" and image.ø == ".":
    res.ø = "#"
  elif rule[511] == "." and image.ø == "#":
    res.ø = "."
  res.extend_shift(1, 1, 1, 1)
  for y in range(0, res.h):
    for x in range(0, res.w):
      res.set(x, y, rule[code(image, x-1, y-1)])
  return res
def enhance_n(image, times):
  for i in range(times):
    image = enhance(image)
  return image
rounds = 2

image = enhance_n(image, 2)
print_res("Part one:", image.count("#"), 1)
image = enhance_n(image, 48)
print_res("Part two:", image.count("#"), 2)
