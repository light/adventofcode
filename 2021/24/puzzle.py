#!/usr/bin/env -S PYTHONPATH=../../util python3

from util import *

def read_prog(filename):
  prog = []
  for l in input_file(filename):
    if l.match("inp (.)"):
      prog.append(f"{l.str(1)} = readinp()")
    elif l.match("add (.) (.+)"):
      prog.append(f"{l.str(1)} += {l.str(2)}")
    elif l.match("mul (.) (.+)"):
      prog.append(f"{l.str(1)} *= {l.str(2)}")
    elif l.match("div (.) (.+)"):
      prog.append(f"{l.str(1)} //= {l.str(2)}")
    elif l.match("mod (.) (.+)"):
      prog.append(f"{l.str(1)} %= {l.str(2)}")
    elif l.match("eql (.) (.+)"):
      prog.append(f"{l.str(1)} = 1 if {l.str(1)} == {l.str(2)} else 0")
    else:
      prog.append(l)
  return compile("\n".join(prog), filename, "exec")

def run_prog(prog, input):
  input = list(input)
  def readinp():
    return input.pop(0)
  loc = {"w": 0, "x": 0, "y": 0, "z": 0, "readinp": readinp}
  exec(prog, globals(), loc)
  return loc["w"], loc["x"], loc["y"], loc["z"]

p1 = read_prog("input_test_1")
r1 = run_prog(p1, [9])

p = read_prog("input")
p_simp = read_prog("input_simp")


# En lisant le code manuellement et fastidieusement, il apparait que le programme utilise z comme une pile,
# et compare le nombre stocké en haut de cette pile avec les nombres en input en fonction de 3 paramètres.
# Pseudo code :
# for op in ops:
#   w = readinput()
#   x = pop() if op[0] else peek()
#   if w != x + op[1]:
#     push(w + op[2])
# Valide <=> pile vide.
#
# We got 7 pop = false, 7 pop = true
ops = []
lines = list(input_file("input"))
for i in range(14):
  lines[i*18+4].match('div z (.+)')
  lines[i*18+5].match('add x (.+)')
  lines[i*18+15].match('add y (.+)')
  ops.append((lines[i*18+4].int(1) == 26, lines[i*18+5].int(1), lines[i*18+15].int(1)))


def emul(input):
  input = input.copy()
  stack = []
  def stack_get(pop): return 0 if not stack else (stack.pop() if pop else stack[-1])
  for op in ops:
    w = input.pop(0)
    if w != stack_get(op[0]) + op[1]:
      stack.append(w + op[2])
  return stack


d = [0] * len(ops)
idx = []
for i, o in enumerate(ops):
  if not o[0]:
    d[i] = 9
    idx.append(i)
  else:
    ref = idx.pop()
    d[i] = d[ref] + ops[ref][2] + o[1]
    if d[i] > 9:
      d[ref] -= d[i] - 9
      d[i] = 9
part_one = d

d = [0] * len(ops)
idx = []
for i, o in enumerate(ops):
  if not o[0]:
    d[i] = 1
    idx.append(i)
  else:
    ref = idx.pop()
    d[i] = d[ref] + ops[ref][2] + o[1]
    if d[i] < 1:
      d[ref] += 1 - d[i]
      d[i] = 1
part_two = d

def check_all(input):
  print(input)
  print(run_prog(p, input))
  print(run_prog(p_simp, input))
  print(emul(input))

check_all([1,3,5,7,9,2,4,6,8,9,9,9,9,9])
check_all(part_one)
check_all(part_two)

print_res("Part one:", "".join([str(d) for d in part_one]), 1)
print_res("Part two:", "".join([str(d) for d in part_two]), 2)
