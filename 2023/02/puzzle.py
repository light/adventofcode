#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
import re

maxRGB = [12, 13, 14]

def parse_play(play):
  rgb = [0, 0, 0]
  for color in play.split(", "):
    n, c = color.split()
    if c == "red":
      rgb[0] = int(n)
    elif c == "green":
      rgb[1] = int(n)
    elif c == "blue":
      rgb[2] = int(n)
  return rgb

def possible(plays):
  for play in plays.split("; "):
    rgb = parse_play(play)
    if rgb[0] > maxRGB[0] or rgb[1] > maxRGB[1] or rgb[2] > maxRGB[2]:
      return False
  return True

score = 0
for l in inputs():
  l.match(r'Game (\d+): (.*)')
  gameId = l.int(1)
  plays = l.str(2)
  if possible(plays):
    score += gameId


print_res("Part one:", score, 1)
