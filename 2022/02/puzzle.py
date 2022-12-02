#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

rules1 = {
  "A X": 1+3,
  "A Y": 2+6,
  "A Z": 3+0,
  "B X": 1+0,
  "B Y": 2+3,
  "B Z": 3+6,
  "C X": 1+6,
  "C Y": 2+0,
  "C Z": 3+3,
}
rules2 = {
  "A X": 0+3,
  "A Y": 3+1,
  "A Z": 6+2,
  "B X": 0+1,
  "B Y": 3+2,
  "B Z": 6+3,
  "C X": 0+2,
  "C Y": 3+3,
  "C Z": 6+1,
}
score1 = 0
score2 = 0
for l in inputs():
  score1 += rules1[l]
  score2 += rules2[l]

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
