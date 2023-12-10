#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P
from path import a_star

board = Board('.')
S = None
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    board.set(x, y, v)
    if v == "S":
      S = board.getP(x, y)


def find_junctures(board, p):
  j = []
  if p.x != 0 and board.get(p.x-1, p.y) in "-LF":
    j.append(board.getP(p.x-1, p.y))
  if p.x != board.w-1 and board.get(p.x+1, p.y) in "-7J":
    j.append(board.getP(p.x+1, p.y))
  if p.y != 0 and board.get(p.x, p.y-1) in "|F7": # Y coords start from the top
    j.append(board.getP(p.x, p.y-1))
  if p.y != board.h-1 and board.get(p.x, p.y+1) in "|JL":
    j.append(board.getP(p.x, p.y+1))
  return j


start, end = find_junctures(board, S)

path, cost = a_star(
  start,
  lambda p: [(n, 1) for n in find_junctures(board, p)],
  lambda p: p == end,
  lambda x: 1)

score1 = int((len(path)+1)/2)

print_res("Part one:", score1, 1)
