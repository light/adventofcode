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


for d in displays:
  guesses = {i:[] for i in range(10)}
  for v in d["values"]:
    for i, s in enumerate(segments):
      if len(s) == len(v):
        guesses[i].append(v)
  guesses[3] = [g for g in guesses[3] if set(g).issuperset(set(guesses[1][0]))]
  guesses[5].remove(guesses[3][0])
  guesses[6] = [g for g in guesses[6] if not set(g).issuperset(set(guesses[1][0]))]
  guesses[9] = [g for g in guesses[9] if set(g).issuperset(set(guesses[3][0]))]
  guesses[0].remove(guesses[6][0])
  guesses[0].remove(guesses[9][0])
  guesses[5] = [g for g in guesses[5] if set(guesses[9][0]).issuperset(set(g))]
  guesses[2].remove(guesses[3][0])
  guesses[2].remove(guesses[5][0])
  guesses = {w[0]:d for d, w in guesses.items()}
  d["decoded"] = int("".join([str(guesses[d]) for d in d["digits"]]))

print("Part one:", sum([1 for d in displays for x in d["digits"] if len(x) in [2,3,4,7]]))
print("Part two:", sum([d["decoded"] for d in displays]))
