#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from functools import cmp_to_key
from typing import NamedTuple

class Bid(NamedTuple):
  hand: str
  bid: int
  type: int

cards = "AKQJT98765432"
Five_of_a_kind = 1
Four_of_a_kind = 2
Full_house = 3
Three_of_a_kind = 4
Two_pair = 5
One_pair = 6
High_card = 7

def parse_bid(l):
  a, b = l.split()
  b = int(b)
  c = list(set([(c, a.count(c)) for c in a]))
  if len(c) == 1:
    return Bid(a, b, Five_of_a_kind)
  elif len(c) == 2:
    if c[0][1] == 4 or c[1][1] == 4:
      return Bid(a, b, Four_of_a_kind)
    else:
      return Bid(a, b, Full_house)
  elif len(c) == 3:
    if c[0][1] == 3 or c[1][1] == 3 or c[2][1] == 3:
      return Bid(a, b, Three_of_a_kind)
    else:
      return Bid(a, b, Two_pair)
  elif len(c) == 4:
    return Bid(a, b, One_pair)
  else:
    return Bid(a, b, High_card)

bids = [parse_bid(l) for l in inputs()]

def cmp_bids(a, b):
  if a.type < b.type:
    return 1
  elif a.type > b.type:
    return -1
  else:
    for i in range(len(a.hand)):
      ca = cards.index(a.hand[i])
      cb = cards.index(b.hand[i])
      if ca > cb:
        return -1
      if ca < cb:
        return 1
    return 0


def score(bids):
  bids = sorted(bids, key=cmp_to_key(cmp_bids))
  score = 0
  for i in range(len(bids)):
    score += (i+1)*bids[i].bid
  return score

print_res("Part one:", score(bids), 1)
