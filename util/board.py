from typing import NamedTuple, Any

class P(NamedTuple):
    x:int
    y:int
    val:Any = None
    def __eq__(self,other):
      return self.x == other.x and self.y == other.y

class Board :
  def __init__(self, ø=0):
    self.board = []
    self.ø = ø
    self.w = self.h = 0
  def extend(self, w, h):
    if w > self.w:
      self.board = [l + [self.ø]*(w-self.w) for l in self.board]
      self.w = w
    if h > self.h:
      self.board = self.board + [[self.ø]*self.w for i in range(h-self.h)]
      self.h = h
  def set(self, x, y, val):
    self.extend(x+1, y+1)
    self.board[y][x] = val
  def get(self, x, y):
    return self.board[y][x]
  def getP(self, x, y):
    return P(x, y, self.board[y][x])
  def print(self):
    for y in range(self.h):
      print("".join([str(self.board[y][x]) for x in range(self.w)]))
  def count(self, val):
    return sum([sum([1 if x == val else 0 for x in l]) for l in self.board])
  def neighbors4(self, p):
    n = []
    if p.x != 0:
      n.append(self.getP(p.x-1, p.y))
    if p.x != self.w-1:
      n.append(self.getP(p.x+1, p.y))
    if p.y != 0:
      n.append(self.getP(p.x, p.y-1))
    if p.y != self.h-1:
      n.append(self.getP(p.x, p.y+1))
    return n
