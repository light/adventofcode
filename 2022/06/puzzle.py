#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *

l = input()

def all_different(*a):
  for i in range(len(a)-1):
    for j in range(i+1,len(a)):
      if a[i] == a[j]:
        return False
  return True
def marker(l, n):
  for i in range(n, len(l)):
    if all_different(*l[i-n:i]):
      return i

def sop(l): return marker(l, 4)
def som(l): return marker(l, 14)

print_res("Part one:", sop(l), 1)
print_res("Part two:", som(l), 2)
