#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board, P

def parsenums(s):
  return [int(i) for i in s.split()]

cards = []
for l in inputs():
  l.match(r"Card +(\d+): (.+) \| (.*)")
  winning = parsenums(l.str(2))
  played = parsenums(l.str(3))
  cards.append([winning, played, 1])


score1 = 0
score2 = 0
for n_card, card in enumerate(cards):
  played, winning, instances = card
  score = 0
  matching_numbers = 0
  for i in played:
    if i in winning:
      score = 1 if score == 0 else score * 2
      matching_numbers += 1
  score1 += score
  score2 += instances
  for j in range(matching_numbers):
    cards[n_card+j+1][2] += instances

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
