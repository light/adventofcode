#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from functools import lru_cache

scanners = []
scanner = None
for l in inputs():
  if l.match('--- scanner (\d+) ---'):
    scanner = []
    scanners.append(scanner)
  elif l.match('(.+),(.+),(.+)'):
    scanner.append((l.int(1), l.int(2), l.int(3)))

### Rotation stuff

# Pre-compute some rotation matrices
#      ⎡ 1     0     0 ⎤            ⎡ 1  0  0 ⎤
# Rx = ⎢ 0  cosϴ -sinϴ ⎥  Rx(90˚) = ⎢ 0  0 -1 ⎥
#      ⎣ 0  sinϴ  cosϴ ⎦            ⎣ 0  1  0 ⎦
#      ⎡ cosϴ  0  sinϴ ⎤            ⎡ 0  0  1 ⎤
# Ry = ⎢ 0     1     0 ⎥  Ry(90˚) = ⎢ 0  1  0 ⎥
#      ⎣ -sinϴ 0  cosϴ ⎦            ⎣-1  0  0 ⎦
#      ⎡ cosϴ -sinϴ  0 ⎤            ⎡ 0 -1  0 ⎤
# Rz = ⎢ sinϴ  cosϴ  0 ⎥  Rz(90˚) = ⎢ 1  0  0 ⎥
#      ⎣    0     0  1 ⎦            ⎣ 0  0  1 ⎦
Rx = [[1,0,0],[0,0,-1],[0,1,0]]
Ry = [[0,0,1],[0,1,0],[-1,0,0]]
Rz = [[0,-1,0],[1,0,0],[0,0,1]]

"""
rot_matrix = [None]*4
for rx in range(4):
  rot_matrix[rx] = [None]*4
  for ry in range
rot_matrix = [1][0][0] =
"""

# Multiplies 2 3x3 matrices
def mmmul(a, b):
  c = [[0,0,0],[0,0,0],[0,0,0]]
  for j in range(3):
    for i in range(3):
      c[i][j] = sum([a[i][k]*b[k][j] for k in range(3)])
  return c
# Multiplies a 3 vector by a 3x3 matrix
def mvmul(a, v):
  return [sum([a[j][i]*v[i] for i in range(3)]) for j in range(3)]
def vadd(v, w):
  return [v[i]+w[i] for i in range(3)]
def vsub(v, w):
  return [v[i]-w[i] for i in range(3)]
@lru_cache(maxsize=None)
def rotmx(rx, ry, rz):
  mx = [[1,0,0],[0,1,0],[0,0,1]]
  for r in range(rz):
    mx = mmmul(mx, Rz)
  for r in range(ry):
    mx = mmmul(mx, Ry)
  for r in range(rx):
    mx = mmmul(mx, Rx)
  return mx
# Angles are expressed in units of 90˚, from 0 to 3
def rotate(coords, rx, ry, rz):
  return mvmul(rotmx(rx, ry, rz), coords)
def rotate_list(coords, rx, ry, rz):
  return [rotate(c, rx, ry, rz) for c in coords]

### Coord matching stuff

# Returns a list of offset and match count according to key for b in a
def match_offsets(coords_a, coords_b, min_count):
  rmin = min(coords_a) - max(coords_b)
  rmax = max(coords_a) - min(coords_b)
  offsets = []
  for d in range(rmin, rmax+1):
    count = 0
    ca = coords_a.copy()
    for b in coords_b:
      for j, a in enumerate(ca):
        if a == b+d:
          count += 1
          ca.pop(j)
          break
      if len(ca) + count < min_count: # Bail out early in case there are not enough elements left to reach min_count
        break
    if count >= min_count:
      offsets.append(d)
  return offsets
# Returns a list of offsets for which at least `min_match` elements match
def find_match_offset(coords_a, coords_b, min_match):
  ca = [[c[i] for c in coords_a] for i in range(3)]
  cb = [[c[i] for c in coords_b] for i in range(3)]
  offsets = [match_offsets(ca[i], cb[i], min_match) for i in range(3)]
  matches = []
  for ox in offsets[0]:
    for oy in offsets[1]:
      count = 0
      for oz in offsets[2]:
        ca = coords_a.copy()
        for b in coords_b:
          for j, a in enumerate(ca):
            if a[0] == b[0]+ox and a[1] == b[1]+oy and a[2] == b[2]+oz:
              count += 1
              ca.pop(j)
              break
      if count >= min_match:
        matches.append([ox, oy, oz])
  return matches

# Rotates b in all possible orientations and returns the orientations and offsets for which
# at least min_match coords match a
def search_match(coords_a, coords_b, min_match):
  matches = []
  for rx in range(4):
    for ry, rz in [(0,0),(0,1),(0,2),(0,3),(1,0),(3,0)]:
      b_rotated = rotate_list(coords_b, rx, ry, rz)
      offsets = find_match_offset(coords_a, b_rotated, min_match)
      if len(offsets) > 1:
        print(offsets)
        raise Exception("More than one offset found, don't know what to do ! :-(")
      if offsets:
        matches.append(([rx, ry, rz], offsets[0]))
  if len(matches) > 1:
    print(matches)
    raise Exception("More than one orientation found, don't know what to do ! :-(")
  return matches[0] if matches else None


offsets = {0:([0,0,0], [0,0,0])}
previous_found = [0]
while len(offsets) != len(scanners):
  found = []
  for testing in [i for i in range(len(scanners)) if not i in offsets]:
    for known in previous_found:
      print("Left", len(scanners)-len(offsets), "Testing", known, testing)
      match = search_match(scanners[known], scanners[testing], 12)
      if match:
        print("Matched", match)
        offsets[testing] = (match[0], vadd(offsets[known][1], match[1]))
        scanners[testing] = rotate_list(scanners[testing], *match[0])
        found.append(testing)
        break
  if not found:
    raise Exception("Found nothing this round !")
  previous_found = found
print(offsets)

unique_coords = set()
for i in offsets:
  rot, off = offsets[i]
  for c in scanners[i]:
    unique_coords.add(tuple(vadd(c, off)))

max_dist = 0
for i in range(len(scanners)):
  for j in range(len(scanners)):
    if i != j:
      o1 = offsets[i][1]
      o2 = offsets[j][1]
      dist = abs(o1[0]-o2[0])+abs(o1[1]-o2[1])+abs(o1[2]-o2[2])
      max_dist = max(dist, max_dist)

print_res("Part one", len(unique_coords), 1)
print_res("Part two", max_dist, 2)
