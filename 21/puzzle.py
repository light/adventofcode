#!/usr/bin/env -S PYTHONPATH=../util pypy3

from util import *
from copy import deepcopy

start = []
for l in inputs():
  if l.match('Player (\d+) starting position: (\d+)'):
    start.append(l.int(2))

def add_mod(a, b, mod):
  a += b
  while a > mod:
    a = a - mod
  return a

class DeterministicDie():
  def __init__(self):
    self.next_throw = 1
    self.throws = 0
  def throw(self):
    throw = self.next_throw
    self.next_throw = add_mod(self.next_throw, 1, 100)
    self.throws += 1
    return throw

def play(players, die):
  while True:
    for p in players:
      move = die.throw()+die.throw()+die.throw()
      p["pos"] = add_mod(p["pos"], move, 10)
      p["score"] += p["pos"]
      if p["score"] >= 1000:
        return

def loser(players):
  for p in players:
    if p["score"] < 1000:
      return p

players_one = [{"pos": p, "score": 0} for p in start]
die = DeterministicDie()
play(players_one, die)
print_res("Part one:", loser(players_one)["score"] * die.throws, 1)

throw_outcomes = [0]*10
for a in range(1, 4):
  for b in range(1, 4):
    for c in range(1, 4):
      throw_outcomes[a+b+c] += 1

def play_outcome(p1, p2):
  outcome = [0, 0]
  for move in range(3, 10):
    new_pos = add_mod(p1[0], move, 10)
    new_score = p1[1] + new_pos
    if new_score >= 21:
      outcome[0] += throw_outcomes[move]
    else :
      o = play_outcome(p2, (new_pos, new_score))
      outcome[0] += o[1] * throw_outcomes[move]
      outcome[1] += o[0] * throw_outcomes[move]
  return outcome

outcome = play_outcome((start[0], 0), (start[1], 0))
print_res("Part two:", max(outcome), 2)
