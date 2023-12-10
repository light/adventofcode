#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *
from functools import reduce

sequences = [
  [int(i) for i in l.split()]
  for l in inputs()
]

def predict_next(seq, backwards = False):
  subseqs = [seq]
  while seq.count(0) != len(seq):
    seq = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    subseqs.append(seq)
  if backwards:
    return reduce(lambda a, b: b-a, [s[0] for s in subseqs[::-1]])
  else:
    return sum([s[-1] for s in subseqs])


score1 = sum([predict_next(s) for s in sequences])
score2 = sum([predict_next(s, backwards=True) for s in sequences])

print_res("Part one:", score1, 1)
print_res("Part two:", score2, 2)
