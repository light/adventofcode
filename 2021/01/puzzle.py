import sys

prev = None
n = 0
for line in sys.stdin:
  val = int(line)
  if prev is not None and val > prev:
    n += 1
  prev = val
print(n)