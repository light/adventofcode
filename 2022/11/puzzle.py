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

for round in range(20):
  for m in monkeys:
    while m['items']:
      m['count'] += 1
      old = m['items'].pop(0)
      new = eval(m['op'])
      new = int(new / 3)
      if new % m['div'] == 0:
        monkeys[m['if_true']]['items'].append(new)
      else:
        monkeys[m['if_false']]['items'].append(new)

#for i, m in enumerate(monkeys):
#  print(f"Monkey {i}: {m['count']} - {m['items']}")

top=sorted(monkeys, key=lambda m: m['count'])[-2:]
score = top[0]['count'] * top[1]['count']
print_res("Part one:", score, 1)

