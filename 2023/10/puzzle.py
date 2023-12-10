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
  lambda x: 0)

loop = [S] + path

score1 = int((len(loop))/2)

# From : https://math.stackexchange.com/questions/3009826/area-of-a-simple-closed-curve
# From : https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Green

def area(loop):
  l = len(loop)
  s = 0
  for i in range(l):
    p1, p2 = loop[i], loop[(i+1)%l]
    s += p1.x*p2.y-p2.x*p1.y
  a = s / 2 # Area from center of cells
  return int(abs(a) - (l-2)/2) # "Heuristically" determined correction ...

assert 0 == area([P(1, 1), P(2, 1), P(2, 2), P(1, 2)])
assert 0 == area([P(1, 1), P(2, 1), P(2, 2), P(2, 3), P(1, 3), P(1, 2)])
assert 0 == area([P(1, 1), P(2, 1), P(3, 1), P(4, 1), P(4, 2), P(3, 2), P(2, 2), P(2, 3), P(3, 3), P(4, 3), P(4, 4), P(3, 4), P(2, 4), P(1, 4), P(1, 3), P(1, 2)])

print_res("Part one:", score1, 1)
print_res("Part two:", area(loop), 2)
