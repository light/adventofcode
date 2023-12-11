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
    self.x0 = self.y0 = 0
    self.w = self.h = 0
  # Extend board to the right and to the bottom so that its dimensions become w, h
  def extend(self, w, h):
    self.extend_shift(right = max(w-self.w, 0), top = max(h-self.h, 0))
  # Extend board by the specified amount of rows or columns in all four directions
  # Base index for rows or columns will be unchanged so if columns are added top or left,
  # existing row indexes will be shifted.
  def extend_shift(self, left=0, bottom=0, right=0, top=0):
    if left == 0 and bottom == 0 and right == 0 and top == 0:
      return
    self.board = [self._null_items(left) + l + self._null_items(right) for l in self.board]
    self.w += left + right
    self.board = [self._null_items(self.w) for i in range(bottom)] + self.board + [self._null_items(self.w) for i in range(top)]
    self.h += top + bottom
  def shift(self, dx, dy):
    self.x0 += dx; self.y0 += dy
  # Insert row at position, shifting rows after it down
  def insertRow(self, y):
    self._check_bounds(self.x0, y)
    self.board = self.board[:y-self.y0] + [self._null_items(self.w)] + self.board[y-self.y0:]
    self.h += 1
  # Insert column at position, shifting columns after it right
  def insertCol(self, x):
    self._check_bounds(x, self.y0)
    self.board = [l[:x-self.x0] + self._null_items(1) + l[x-self.x0:] for l in self.board]
    self.w += 1
  # Sets value at coordinates, extending board as needed.
  def set(self, x, y, val):
    self.extend_shift(left=max(self.x0-x, 0), bottom=max(self.y0-y, 0), right=max(x-self.x0+1-self.w, 0), top=max(y-self.y0+1-self.h, 0))
    self.shift(min(x-self.x0, 0), min(y-self.y0, 0))
    self.board[y-self.y0][x-self.x0] = val
  def get(self, x, y):
    self._check_bounds(x, y)
    return self.board[y-self.y0][x-self.x0]
  def getP(self, x, y):
    return P(x, y, self.get(x, y))
  def print(self, flipY=False):
    print(f"> Map origin ({self.x0},{self.y0}), size ({self.w},{self.h})")
    for y in range(len(self.board)-1, -1, -1) if flipY else range(len(self.board)):
      print("".join([str(self.board[y][x]) for x in range(len(self.board[y]))]))
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
  def visit(self, visitor, acc=None):
    for x in range(self.x0, self.x0+self.w):
      for y in range(self.y0, self.y0+self.h):
        acc = visitor(acc, x, y, self.get(x, y))
    return acc
  def copy(self):
    n = Board()
    n.board = [[v for v in l] for l in self.board]
    n.ø = self.ø; n.w = self.w; n.h = self.h
    return n
  def _null_items(self, n):
    return [self.ø() for i in range(n)] if callable(self.ø) else [self.ø]*n
  def _check_bounds(self, x, y):
    if x >= self.x0+self.w or y >= self.y0+self.h or x < self.x0 or y < self.y0:
      raise IndexError(f"{x},{y} out of bounds: origin ({self.x0},{self.y0}), size ({self.w},{self.h})")
  def __eq__(s, o):
    return isinstance(o, s.__class__) and s.ø == o.ø and s.board == o.board