#!/usr/bin/env -S PYTHONPATH=../util python3

from util import *
from functools import reduce

TYPE_LITERAL = 4
TYPE_SUM = 0
TYPE_PRODUCT = 1
TYPE_MINIMUM = 2
TYPE_MAXIMUM = 3
TYPE_GREATER_THAN = 5
TYPE_LESS_THAN = 6
TYPE_EQUAL_TO = 7

class BitStream:
  def __init__(self, hex=None, bits=None):
    if bits:
      self.bits = bits
    else:
      self.bits = list(format(int(hex, 16), f"0{len(hex)*4}b"))
  def int(self, nb_bits):
    i = 0
    for b in range(nb_bits):
      i = (i<<1) + int(self.bits.pop(0))
    return i
  def literal(self):
    i = 0
    while True:
      more = self.int(1)
      i = (i<<4) + self.int(4)
      if more == 0:
        return i
  def empty(self):
    return not self.bits
  def sub(self, len):
    sub = BitStream(bits=self.bits[:len])
    self.bits = self.bits[len:]
    return sub

bs = BitStream(next(inputs()))

def read_packet(bs):
  version = bs.int(3)
  type = bs.int(3)
  if type == TYPE_LITERAL:
    return (version, type, bs.literal())
  else:
    len_type = bs.int(1)
    args = []
    if len_type == 0:
      len_bits = bs.int(15)
      sub = bs.sub(len_bits)
      while not sub.empty():
        args.append(read_packet(sub))
    else:
      len_packets = bs.int(11)
      for i in range(len_packets):
        args.append(read_packet(bs))
    return (version, type, args)


def sum_of_versions(packet):
  s = packet[0]
  if packet[1] != TYPE_LITERAL:
    s += sum([sum_of_versions(p) for p in packet[2]])
  return s

def evaluate(packet):
  t = packet[1]
  if t == TYPE_LITERAL:
    return packet[2]
  elif t == TYPE_SUM:
    return sum([evaluate(p) for p in packet[2]])
  elif t == TYPE_PRODUCT:
    return reduce(lambda a,b: a*b, [evaluate(p) for p in packet[2]], 1)
  elif t == TYPE_MINIMUM:
    return min([evaluate(p) for p in packet[2]])
  elif t == TYPE_MAXIMUM:
    return max([evaluate(p) for p in packet[2]])
  elif t == TYPE_GREATER_THAN:
    return 1 if evaluate(packet[2][0]) > evaluate(packet[2][1]) else 0
  elif t == TYPE_LESS_THAN:
    return 1 if evaluate(packet[2][0]) < evaluate(packet[2][1]) else 0
  elif t == TYPE_EQUAL_TO:
    return 1 if evaluate(packet[2][0]) == evaluate(packet[2][1]) else 0
  else:
    1/0


packet = read_packet(bs)

print_res("Part one", sum_of_versions(packet), 1)
print_res("Part two", evaluate(packet), 2)
