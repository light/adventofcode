#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *

monkeys = []
inp = list(inputs())
while inp:
  inp.pop(0)
  monkey = {
    "items": [int(i) for i in inp.pop(0)[18:].split(", ")],
    "op": inp.pop(0)[19:],
    "div": int(inp.pop(0)[21:]),
    "if_true": int(inp.pop(0)[29:]),
    "if_false": int(inp.pop(0)[30:]),
    "count": 0
  }
  monkeys.append(monkey)
  if inp:
    inp.pop(0)

def monkey_business(monkeys, rounds, worry_a_lot=False) :
  k = 1
  for m in monkeys:
      k *= m['div']
  for round in range(rounds):
    for m in monkeys:
      while m['items']:
        m['count'] += 1
        old = m['items'].pop(0)
        new = eval(m['op'])
        if not worry_a_lot:
          new = int(new / 3)
        else:
          new = new % k
        if new % m['div'] == 0:
          monkeys[m['if_true']]['items'].append(new)
        else:
          monkeys[m['if_false']]['items'].append(new)
  top = sorted(monkeys, key=lambda m: m['count'])[-2:]
  return top[0]['count'] * top[1]['count']

import copy
tmp = copy.deepcopy(monkeys)
print_res("Part one:", monkey_business(tmp, 20), 1)
print_res("Part two:", monkey_business(monkeys, 10000, True), 2)

