#!/usr/bin/env python3

import sys

x = y = 0
for line in sys.stdin:
  cmd, val = line.split(" ")
  val = int(val)
  if cmd == "forward":
    x += val
  if cmd == "down":
    y += val
  if cmd == "up":
    y -= val

print(x*y)