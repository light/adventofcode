#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *

class Cuboid:
  def __init__(self, x1, x2, y1, y2, z1, z2):
    self.x1 = x1; self.x2 = x2; self.y1 = y1; self.y2 = y2; self.z1 = z1; self.z2 = z2
  def __repr__(s):
    return f"{s.x1}..{s.x2},{s.y1}..{s.y2},{s.z1}..{s.z2}"
  def volume(s):
    return (s.x2-s.x1+1)*(s.y2-s.y1+1)*(s.z2-s.z1+1)
  def is_inside(s, o):
    return s.x1 >= o.x1 and s.x2 <= o.x2 and s.y1 >= o.y1 and s.y2 <= o.y2 and s.z1 >= o.z1 and s.z2 <= o.z2
  def intersects(s, o):
    return s.x2 >= o.x1 and s.x1 <= o.x2 and s.y2 >= o.y1 and s.y1 <= o.y2 and s.z2 >= o.z1 and s.z1 <= o.z2
  def sub(s, o):
    if not s.intersects(o):
      return [s]
    elif o.x1 > s.x1:
      return Cuboid(s.x1, o.x1-1, s.y1, s.y2, s.z1, s.z2).sub(o) + Cuboid(o.x1, s.x2, s.y1, s.y2, s.z1, s.z2).sub(o)
    elif o.x2 < s.x2:
      return Cuboid(s.x1, o.x2, s.y1, s.y2, s.z1, s.z2).sub(o) + Cuboid(o.x2+1, s.x2, s.y1, s.y2, s.z1, s.z2).sub(o)
    elif o.y1 > s.y1:
      return Cuboid(s.x1, s.x2, s.y1, o.y1-1, s.z1, s.z2).sub(o) + Cuboid(s.x1, s.x2, o.y1, s.y2, s.z1, s.z2).sub(o)
    elif o.y2 < s.y2:
      return Cuboid(s.x1, s.x2, s.y1, o.y2, s.z1, s.z2).sub(o) + Cuboid(s.x1, s.x2, o.y2+1, s.y2, s.z1, s.z2).sub(o)
    elif o.z1 > s.z1:
      return Cuboid(s.x1, s.x2, s.y1, s.y2, s.z1, o.z1-1).sub(o) + Cuboid(s.x1, s.x2, s.y1, s.y2, o.z1, s.z2).sub(o)
    elif o.z2 < s.z2:
      return Cuboid(s.x1, s.x2, s.y1, s.y2, s.z1, o.z2).sub(o) + Cuboid(s.x1, s.x2, s.y1, s.y2, o.z2+1, s.z2).sub(o)
    # Cuboids must be equal here
    return []

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
