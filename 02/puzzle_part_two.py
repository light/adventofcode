#!/usr/bin/env python3

import sys

x = y = aim = 0
for line in sys.stdin:
  cmd, val = line.split(" ")
  val = int(val)
  if cmd == "forward":
    x += val
    y += val * aim
  if cmd == "down":
    aim += val
  if cmd == "up":
    aim -= val

print(x*y)