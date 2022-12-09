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
    if w > self.w or h > self.h:
      self.extend_shift(right = max(w-self.w, 0), bottom = max(h-self.h, 0))
  def extend_shift(self, left=0, top=0, right=0, bottom=0):
    self.board = [self._null_items(left) + l + self._null_items(right) for l in self.board]
    self.w += left + right
    self.board = [self._null_items(self.w) for i in range(top)] + self.board + [self._null_items(self.w) for i in range(bottom)]
    self.h += top + bottom
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
  def copy(self):
    n = Board()
    n.board = [[v for v in l] for l in self.board]
    n.ø = self.ø; n.w = self.w; n.h = self.h
    return n
  def _null_items(self, n):
    return [self.ø() for i in range(n)] if callable(self.ø) else [self.ø]*n
  def __eq__(s, o):
    return isinstance(o, s.__class__) and s.ø == o.ø and s.board == o.board