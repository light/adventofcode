#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from functools import cmp_to_key
from typing import NamedTuple

class Bid(NamedTuple):
  hand: str
  bid: int
  type: int

cards1 = "AKQJT98765432"
cards2 = "AKQT98765432J"
Five_of_a_kind = 1
Four_of_a_kind = 2
Full_house = 3
Three_of_a_kind = 4
Two_pair = 5
One_pair = 6
High_card = 7

def rules1(hand):
  c = list(set([(c, hand.count(c)) for c in hand]))
  if len(c) == 1:
    return Five_of_a_kind
  elif len(c) == 2:
    if c[0][1] == 4 or c[1][1] == 4:
      return Four_of_a_kind
    else:
      return Full_house
  elif len(c) == 3:
    if c[0][1] == 3 or c[1][1] == 3 or c[2][1] == 3:
      return Three_of_a_kind
    else:
      return Two_pair
  elif len(c) == 4:
    return One_pair
  else:
    return High_card

def rules2(hand):
  jokers = hand.count("J")
  hand = hand.replace("J", "")
  c = list(set([(c, hand.count(c)) for c in hand]))
  c.sort(key=lambda x: x[1])
  if jokers == 5:
    c = [("A", 0)]
  c[-1] = (c[-1][0], c[-1][1]+jokers)

  if len(c) == 1:
    return Five_of_a_kind
  elif len(c) == 2:
    if c[0][1] == 4 or c[1][1] == 4:
      return Four_of_a_kind
    else:
      return Full_house
  elif len(c) == 3:
    if c[0][1] == 3 or c[1][1] == 3 or c[2][1] == 3:
      return Three_of_a_kind
    else:
      return Two_pair
  elif len(c) == 4:
    return One_pair
  else:
    return High_card


def parse_bid(l, rules):
  a, b = l.split()
  return Bid(a, int(b), rules(a))


bids = [l for l in inputs()]

def cmp_bids(a, b, cards):
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


def score(bids, rules, cards):
  bids = [parse_bid(bid, rules) for bid in bids]
  bids = sorted(bids, key=cmp_to_key(lambda a, b: cmp_bids(a, b, cards)))
  score = 0
  for i in range(len(bids)):
    score += (i+1)*bids[i].bid
  return score

print_res("Part one:", score(bids, rules1, cards1), 1)
print_res("Part one:", score(bids, rules2, cards2), 2)
