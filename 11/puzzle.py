#!/usr/bin/env python3

import sys
from collections import namedtuple

P = namedtuple("P", ["x", "y"])

octo = []
for l in sys.stdin:
  octo.append([int(i) for i in l.strip()])
w = len(octo[0])
h = len(octo)

def neighbors(p):
   n = []
   for i in range(-1, 2):
     for j in range(-1, 2):
        nx = p.x+i; ny = p.y+j
        if (i!=0 or j!=0) and nx>=0 and nx<w and ny>=0 and ny<h:
           n.append(P(nx, ny))
   return n

def printo(octo):
   for y in range(h):
      print("".join([str(octo[y][x]) for x in range(w)]))

def step(octo):
   new = [[o+1 for o in l] for l in octo]
   do_flashes = True
   flashed = []
   while do_flashes:
      do_flashes = False
      for x in range(w):
         for y in range(h):
            p = P(x, y)
            if new[y][x] > 9 and p not in flashed:
               flashed.append(p)
               do_flashes = True
               for n in neighbors(p):
                  new[n.y][n.x] += 1
   for p in flashed:
      new[p.y][p.x] = 0
   return new, len(flashed)

flashes = 0
for i in range(100):
   octo, f = step(octo)
   flashes += f

flashed = 0; i = 100
while flashed != 100:
   octo, flashed = step(octo)
   i += 1


print("Part one:", flashes)
print("Part two:", i)
