#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
import sys

class Board :
  def __init__(self, ø=0):
    self.board = []
    self.ø = ø
    self.w = self.h = 0
  def extend(self, w, h):
    if w > self.w:
      self.board = [l + [self.ø]*(w-self.w) for l in self.board]
      self.w = w
    if h > self.h:
      self.board = self.board + [[self.ø]*self.w for i in range(h-self.h)]
      self.h = h
  def set(self, x, y, val):
    self.extend(x+1, y+1)
    self.board[y][x] = val
  def print(self):
    for y in range(self.h):
      print("".join([str(self.board[y][x]) for x in range(self.w)]))
  def __fuse(self, a, b):
    return [p[1] if p[1] is not self.ø else p[0] for p in zip(a, b)]
  def fold_along(self, dim, pos):
    if dim == "x":
      a = pos*2-self.w+1
      self.board = [l[:a] + self.__fuse(l[a:pos], list(reversed(l[pos+1:]))) for l in self.board]
      self.w = pos
    else:
      a = pos*2-self.h+1
      self.board = self.board[:a] + [self.__fuse(self.board[y], self.board[pos*2-y]) for y in range(a, pos)]
      self.h = pos
  def count(self, val):
    return sum([sum([1 if x == val else 0 for x in l]) for l in self.board])

board = Board("░")
folds = []
for l in inputs():
  if l.match('(\d+),(\d+)'):
    board.set(l.int(1), l.int(2), "█")
  elif l.match('fold along (.)=(\d+)'):
    folds.append((l.str(1), l.int(2)))


board.fold_along(*folds[0])
part_one = board.count("█")
for fold in folds[1:]:
  board.fold_along(*fold)

print_res("Part one:", part_one, 1)
board.print()
