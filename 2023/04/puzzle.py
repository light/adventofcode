#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

def parsenums(s):
  return [int(i) for i in s.split()]

score1 = 0
for l in inputs():
  l.match(r"Card +(\d+): (.+) \| (.*)")
  winning = parsenums(l.str(2))
  played = parsenums(l.str(3))
  score = 0
  for i in played:
    if i in winning:
      score = 1 if score == 0 else score * 2
  score1 += score

print_res("Part one:", score1, 1)
