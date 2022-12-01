#!/usr/bin/env python3

import sys

counts = None
n = 0
for line in sys.stdin:
  if counts is None:
    counts = [0] * (len(line)-1)
  for i in range(0, len(counts)):
    if line[i] == "1":
      counts[i] += 1
  n += 1

a = "".join(["1" if count >= n/2 else "0" for count in counts])
b = "".join(["0" if count >= n/2 else "1" for count in counts])
gamma = int(a, 2)
epsilon = int(b, 2)
print(gamma*epsilon)
