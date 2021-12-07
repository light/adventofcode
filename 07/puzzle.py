#!/usr/bin/env python3

import sys

crabs = [int(i) for i in sys.stdin.read().strip().split(",")]
def fuel_use(crabs, pos, fuel_function): return sum([fuel_function(abs(c - pos)) for c in crabs])
def least_fuel(crabs, fuel_function): return min([fuel_use(crabs, pos, fuel_function) for pos in range(min(crabs), max(crabs)+1)])
def fuel_function_1(d): return d
def fuel_function_2(d): return d*(d+1)/2

print("Part one:", least_fuel(crabs, fuel_function_1))
print("Part two:", least_fuel(crabs, fuel_function_2))
