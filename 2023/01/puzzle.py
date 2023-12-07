#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
import re

numbers = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

def first_digit(l, reverse=False):
  if reverse:
    l = l[::-1]
  for i in range(len(l)):
    s = l[i:]
    if(s[0].isdigit()):
      return s[0]
    for k, v in numbers.items():
      if reverse:
        k = k[::-1]
      if s.startswith(k):
        return v

s = 0
for l in inputs():
  s += int(first_digit(l)+first_digit(l, True))

print_res("Part one:", s, 1)
print_res("Part two:", s, 2)
