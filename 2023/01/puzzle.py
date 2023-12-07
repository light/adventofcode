#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
import re

s = 0
for l in inputs():
  digits = re.findall(r'\d', l)
  s += int(digits[0]+digits[-1])

print_res("Part one:", s, 1)
