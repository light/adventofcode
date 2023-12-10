#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

sequences = [
  [int(i) for i in l.split()]
  for l in inputs()
]

def predict_next(seq):
  subseqs = [seq]
  while seq.count(0) != len(seq):
    seq = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    subseqs.append(seq)
  return sum([s[-1] for s in subseqs])


def score1(seqs):
  return sum([predict_next(s) for s in seqs])

print_res("Part one:", score1(sequences), 1)
