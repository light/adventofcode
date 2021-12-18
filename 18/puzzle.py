#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
from math import floor, ceil

class Spair():
  def __init__(self, l, r):
    self.l = l
    self.r = r
  def set(self, side, val):
    if side == "L":
      self.l = val
    else:
      self.r = val
  def side(self, s):
    return self.l if s == "L" else self.r
  def magnitude(self):
    return 3*self.l.magnitude() + 2*self.r.magnitude()
  def __repr__(self):
    return "("+str(self.l)+","+str(self.r)+")"
class Sleaf():
  def __init__(self, val):
    self.val = val
  def magnitude(self):
    return self.val
  def __repr__(self):
    return str(self.val)
class Snum():
  def __init__(self, repr):
    self.pair = self.__parse(list(repr))
  def __parse(self, chars):
    c = chars.pop(0)
    if c == '[':
      left = self.__parse(chars)
      chars.pop(0) # ","
      right = self.__parse(chars)
      chars.pop(0) # "]"
      return Spair(left, right)
    else:
      return Sleaf(int(c))
  def add(self, other):
    self.pair = Spair(self.pair, other.pair)
    while True:
      nested = self.find_nested(self.pair)
      if nested is not None:
        self.explode(*nested)
        continue
      splittable = self.find_splittable(self.pair)
      if splittable is not None:
        val = splittable[0].val
        self.set(splittable[1], Spair(Sleaf(floor(val/2)), Sleaf(ceil(val/2))))
        continue
      break
  def find_nested(self, node, depth=4, ch=""):
    if type(node) == Spair:
      if depth == 0:
        return (node, ch)
      else:
        return self.find_nested(node.l, depth-1, ch+"L") or self.find_nested(node.r, depth-1, ch+"R")
    return None
  def find_splittable(self, node, ch=""):
    if type(node) == Spair:
      return self.find_splittable(node.l, ch+"L") or self.find_splittable(node.r, ch+"R")
    return (node, ch) if node.val > 9 else None
  def find_next_to(self, chain, side):
    invside = "R" if side == "L" else "L"
    idx = chain.rfind(invside)
    if idx != -1:
      p = self.pair
      for s in chain[:idx]:
        p = p.side(s)
      p = p.side(side)
      while type(p) is Spair:
        p = p.side(invside)
      return p
  def set(self, chain, val):
    p = self.pair
    for s in chain[:-1]:
      p =  p.side(s)
    p.set(chain[-1], val)
  def explode(self, p, chain):
    l = self.find_next_to(chain, "L")
    r = self.find_next_to(chain, "R")
    if l is not None:
      l.val += p.l.val
    if r is not None:
      r.val += p.r.val
    self.set(chain, Sleaf(0))
  def magnitude(self):
    return self.pair.magnitude()
  def __repr__(self):
    return self.__repr(self.pair)
  def __repr(self, p):
    if type(p) is Spair:
      return "[" + self.__repr(p.l) + "," + self.__repr(p.r) + "]"
    else:
      return str(p)

nums = list(inputs())
part_one = None
for l in nums:
  if part_one is None:
    part_one = Snum(l)
  else:
    part_one.add(Snum(l))

best = 0
for i, a in enumerate(nums):
  for j, b in enumerate(nums):
    if i != j:
      n = Snum(a)
      n.add(Snum(b))
      best = max(best, n.magnitude())


print_res("Part one", part_one.magnitude(), 1)
print_res("Part two", best, 2)
