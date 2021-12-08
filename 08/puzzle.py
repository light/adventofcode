#!/usr/bin/env python3

import sys

segments = [
  "abcefg",
  "cf",
  "acdeg",
  "acdfg",
  "bcdf",
  "abdfg",
  "abdefg",
  "acf",
  "abcdefg",
  "abcdfg"
]

displays = []
for l in sys.stdin:
  a, b = l.split(" | ")
  displays.append({
    "values": ["".join(sorted(v)) for v in a.split()],
    "digits": ["".join(sorted(v)) for v in b.split()]
  })

# First pass, guess possibilities by number of segments
def guess_by_number_of_lit_segments(values):
  guesses = {}
  for v in values:
    guesses[v] = [i for i, s in enumerate(segments) if len(s) == len(v)]
  return guesses
for d in displays:
  d["guesses"] = guess_by_number_of_lit_segments(d["values"])

score_part_1 = 0
for d in displays:
  for digit in d["digits"]:
    if len(d["guesses"][digit]) == 1:
      score_part_1 += 1
print(score_part_1)
