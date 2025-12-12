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
    # Cuboid to sub must be equal or larger here
    return []

# Segment of integers, both bounds are inclusive.
class Segment:
  def __init__(self, x1, x2):
    self.x1 = x1
    self.x2 = x2
  def __eq__(self, o):
    return isinstance(o, Segment) and self.x1 == o.x1 and self.x2 == o.x2
  def __repr__(s):
    return f"{s.x1}..{s.x2}"
  def length(self):
    return self.x2 - self.x1 + 1
  def is_inside(self, x):
    return self.x1 <= x and x <= self.x2
  def intersects(s, o):
    return s.x2 >= o.x1 and s.x1 <= o.x2
  def sub(s, o):
    if not s.intersects(o):
      return [s]
    if o.x1 > s.x1 and o.x2 < s.x2:
      return [Segment(s.x1, o.x1-1), Segment(o.x2+1, s.x2)]
    elif o.x1 > s.x1:
      return [Segment(s.x1, o.x1-1)]
    elif o.x2 < s.x2:
      return [Segment(o.x2+1, s.x2)]
    return []
