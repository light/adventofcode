#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from geom import Cuboid

steps = []
for l in inputs():
  if l.match('(on|off) x=(.+)\.\.(.+),y=(.+)\.\.(.+),z=(.+)\.\.(.+)'):
    steps.append((l.str(1), Cuboid(l.int(2), l.int(3), l.int(4), l.int(5), l.int(6), l.int(7))))

def volume(cuboids):
  return sum([a.volume() for a in cuboids])

def sub_all(cuboid, others):
  res = [cuboid]
  for o in others:
    tmp = []
    for c in res:
      tmp += c.sub(o)
    res = tmp
  return res

small_box = Cuboid(-50, 50, -50, 50, -50, 50)
def lit_cubes(steps):
  cuboids = []
  for s in steps:
    if s[0] == "on":
      cuboids += sub_all(s[1], cuboids)
    else:
      cuboids = sum([c.sub(s[1]) for c in cuboids], [])
  return volume(cuboids)

print_res("Part one:", lit_cubes(filter(lambda s: s[1].is_inside(small_box), steps)), 1)
print_res("Part two:", lit_cubes(steps), 2)
