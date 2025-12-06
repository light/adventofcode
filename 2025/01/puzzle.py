#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

steps = []
for step in inputs():
  n = int(step[1:])
  if step[0] == "L":
    steps.append(-n)
  else:
    steps.append(n)

pos = 50
score1 = 0

for step in steps:
  pos = (pos+step) % 100
  if pos == 0:
    score1 += 1

print_res("Part one:", score1, 1)

def part_two(steps):
  pos = 50
  score = 0
  for step in steps:
    full_turns = abs(step) // 100
    score += full_turns
    step += full_turns * (100 if step < 0 else -100)
    pos += step
    if pos < 0:
      pos += 100
      score += 1
    elif pos > 99:
      pos -= 100
      score += 1
  return score

# Last resort since my other attempts failed ...
def part_two_brute_force(steps):
  pos = 50
  score = 0
  for step in steps:
    while step > 0:
      step -= 1
      pos += 1
      if pos == 100:
        pos = 0
      if pos == 0:
        score += 1
    while step < 0:
      step += 1
      pos -= 1
      if pos == -1:
        pos = 99
      if pos == 0:
        score += 1
  return score

score2 = part_two(steps)
score2 = part_two_brute_force(steps)
print_res("Part two:", score2, 2)