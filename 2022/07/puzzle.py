#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *

def empty_dir(parent): return { "dirs": {}, "size": 0, "parent": parent }
root = empty_dir(None)
cwd = None
for l in inputs():
  if l.match('\$ cd (.+)'):
    dir = l.str(1)
    if dir == "/":
      cwd = root
    elif dir == "..":
      cwd = cwd["parent"]
    else:
      cwd = cwd["dirs"][dir]
  elif l.match('\$ ls'):
    pass
  elif l.match('dir (.+)'):
      cwd["dirs"][l.str(1)] = empty_dir(cwd)
  elif l.match('(\d+) .+'):
    d = cwd
    while d is not None:
      d["size"] += l.int(1)
      d = d["parent"]

def walk(cwd, fun, acc=None):
  if cwd is None:
    return acc
  acc = fun(acc, cwd)
  for dir in cwd["dirs"].values():
    acc = walk(dir, fun, acc)
  return acc

size_less_than_10k = walk(root, lambda sum, dir: sum+dir["size"] if dir["size"] <= 100000 else sum, 0)
print_res("Part one:", size_less_than_10k, 1)

TOTAL_SIZE = 70000000
SPACE_NEEDED = 30000000
space_left = TOTAL_SIZE - root["size"]
to_delete = SPACE_NEEDED - space_left
dir_to_delete = walk(root, lambda best, dir: dir if dir["size"] >= to_delete and dir["size"] < best["size"] else best, root)

print_res("Part two:", dir_to_delete["size"], 2)
