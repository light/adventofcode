#!/usr/bin/env python3

import sys

markers = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]
points_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
points_2 = {")": 1, "]": 2, "}": 3, ">": 4}

def get_marker(c):
  return next((m for m in markers if m[0] == c), None)
def parse_line(l):
  groups = []
  for c in l:
    m = get_marker(c)
    if m:
      groups.append(m)
    else:
      if not groups:
        return (False, c)
      else:
        m = groups.pop()
        if m[1] != c:
          return (False, c)
  return (True, groups)

score_1 = 0
scores_2 = []
for l in sys.stdin:
  ok, res = parse_line(l.strip())
  if not ok :
    score_1 += points_1[res]
  else:
    score_2 = 0
    while res:
      score_2 *= 5
      score_2 += points_2[res.pop()[1]]
    scores_2.append(score_2)

print("Part one:", score_1)
print("Part two:", sorted(scores_2)[int(len(scores_2)/2)])
