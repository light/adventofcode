#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *

l = next(inputs())
l.match('target area: x=(.+)\.\.(.+), y=(.+)\.\.(.+)')
xmin = l.int(1); xmax = l.int(2); ymin = l.int(3); ymax = l.int(4)

# y_t+1 = y_t + vy_t
# y_0 = 0
# vy_t+1 = vy_t - 1
# => vy_t = vy_0 - t
# => y_1 = vy_0
#    y_2 = vy_0 + vy_0 - 1
#    y_3 = 3*vy_0 - 2
# => y_t = t*vy_0 - t*(t-1)/2

# x_t+1 = x_t + vx_t
# x_0 = 0
# vx_t+1 = vx_t + (vx_t > 0 ? 1 : 0) # Assume positive vx
# => vx_t = t < vx_0 ? vx_0 - t : 0
# => x_t = t*vx_0 - t(t-1)/2 | t < vx_0
#    x_t = vx_0^2 - vx_0(vx_0-1)/2 | t >= vx_0
#    x_t = vx_0(vx_0+1)/2 | t >= vx_0

def x(vx_0, t): return t*vx_0 - t*(t-1)//2 if t < vx_0 else vx_0*(vx_0+1)//2
def y(vy_0, t): return t*vy_0 - t*(t-1)//2

maxy = 0
count = 0
ok = []
for vx_0 in range(1000):
  for vy_0 in range(ymin, 1000):
    t = 0
    _x = _y = _maxy = 0
    while _x <= xmax and _y >= ymin:
      _x = x(vx_0, t)
      _y = y(vy_0, t)
      _maxy = max(_maxy, _y)
      if _x <= xmax and _x >= xmin and _y >= ymin and _y <= ymax:
        maxy = max(maxy, _maxy)
        count += 1
        ok.append((vx_0, vy_0))
        break
      t += 1

print_res("Part one", maxy, 1)
print_res("Part two", count, 2)
