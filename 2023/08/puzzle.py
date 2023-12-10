#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

inp = inputs()

rules = next(inp)
next(inp)
graph = {}
for l in inp:
  l.match(r"(.{3}) = \((.{3}), (.{3})\)")
  graph[l.str(1)] = (l.str(2), l.str(3))

node = "AAA"

rule_idx = 0
while node != "ZZZ":
  if rules[rule_idx%len(rules)] == "L":
    node = graph[node][0]
  else:
    node = graph[node][1]
  rule_idx += 1

print_res("Part one:", rule_idx, 1)
