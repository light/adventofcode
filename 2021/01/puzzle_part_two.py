import sys

prev = None
window = []
n = 0
for line in sys.stdin:
  window.append(int(line))
  if len(window) == 3:
    val = sum(window)
    if prev is not None and val > prev:
      n += 1
    prev = val
    window.pop(0)

print(n)