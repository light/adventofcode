#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

from board import Board, P
from path import a_star

board = Board('.')
S, E = None, None
for y, l in enumerate(inputs()):
  for x, v in enumerate(l):
    board.set(x, y, v)
    if v == "S":
      S = board.getP(x, y)
    if v == "E":
      E = board.getP(x, y)


def find_next_level(board, p):
  current_level = ord("a" if p.val == "S" else p.val)
  n = []
  def test(x, y):
    v = board.get(x, y)
    level = ord("z" if v == "E" else v)
    return level <= current_level + 1
  if p.x != 0 and test(p.x-1, p.y):
    n.append(board.getP(p.x-1, p.y))
  if p.x != board.w-1 and test(p.x+1, p.y):
    n.append(board.getP(p.x+1, p.y))
  if p.y != 0 and test(p.x, p.y-1):
    n.append(board.getP(p.x, p.y-1))
  if p.y != board.h-1 and test(p.x, p.y+1):
    n.append(board.getP(p.x, p.y+1))
  return n


path, cost = a_star(
  S,
  lambda p: [(n, 1) for n in find_next_level(board, p)],
  lambda p: p == E,
  lambda x: 0)

score1 = len(path)-1

print_res("Part one:", score1, 1)
