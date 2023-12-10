#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

inp = inputs()

rules = next(inp)
next(inp)
graph = {}
for l in inp:
  l.match(r"(.{3}) = \((.{3}), (.{3})\)")
  graph[l.str(1)] = (l.str(2), l.str(3))


def score1(graph, node, end_reached):
  rule_idx = 0
  while not end_reached(node):
    if rules[rule_idx%len(rules)] == "L":
      node = graph[node][0]
    else:
      node = graph[node][1]
    rule_idx += 1
  return rule_idx

def primes():
  previous = []
  i = 2
  while True:
    divisible = False
    for p in previous:
      if i % p == 0:
        divisible = True
        break
    if not divisible:
      previous.append(i)
      yield i
    i += 1

def ppcm(numbers):
  res = 1
  for p in primes():
    if sum(numbers) == len(numbers):
      return res
    try_p = True
    while try_p:
      try_p = False
      for i in range(len(numbers)):
        if numbers[i] % p == 0:
          numbers[i] /= p
          try_p = True
      if try_p:
        res *= p
  raise "Algo error"

def score2(graph):
  nodes = list(filter(lambda x: x[2] == "A", graph.keys()))
  end_reached = lambda x: x[2] == "Z"
  P = [score1(graph, node, end_reached) for node in nodes]
  return ppcm(P)

assert ppcm([4, 7, 12, 21, 42]) == 84

if cmdline_arg(1) == "camel":
  print_res("Part one:", score1(graph, "AAA", lambda x: x == "ZZZ"), 2)
if cmdline_arg(1) == "ghost":
  print_res("Part one:", score2(graph), 2)
