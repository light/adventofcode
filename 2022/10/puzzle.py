#!/usr/bin/env -S PYTHONPATH=../../util pypy3

from util import *
from board import Board

CY = {"noop": 1, "addx": 2}
class CPU:
  def __init__(self, program):
    self.program = program
    self.reset()
  def run(self, cycles):
    ran_cycles = 0
    while ran_cycles < cycles:
      if self.cy == 0 and self.instr[:4] == "addx":
        self.w += int(self.instr[5:])
      if self.instr is None or self.cy == 0:
        if self.pc == len(self.program):
          break
        self._load()
      self.cy -= 1
      ran_cycles += 1
    return ran_cycles
  def reset(self):
    self.w = 1
    self.pc = 0
    self.instr = None
    self._load()
  def _load(self):
    self.instr = self.program[self.pc]
    self.cy = CY[self.instr[:4]]
    self.pc += 1

cpu = CPU([i for i in inputs()])

cy = 20
score = 0
cpu.run(20)
while True:
  score += cy * cpu.w
  if cpu.run(40) < 40:
    break
  cy += 40

print_res("Part one:", score, 1)

cpu.reset()

screen = Board('.')
for y in range(6):
  for x in range(40):
    cpu.run(1)
    if x >= cpu.w-1 and x <= cpu.w+1:
      screen.set(x, y, '#')
print("Part two:")
screen.print(flipY=True)
