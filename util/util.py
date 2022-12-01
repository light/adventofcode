#!/usr/bin/env python3

import sys
import re

def print_res(msg, val, exp_arg):
  expected = int(sys.argv[exp_arg]) if len(sys.argv) > exp_arg and sys.argv[exp_arg] != "_" else None
  if expected is not None:
    okko = "\033[92mOK!\033[0m" if val == expected else f"\033[91mKO!\033[0m (expected {expected})"
    print(msg, val, okko)
  else:
    print(msg, val)

# Convenience class to cut a line of text into parts
# Cut on regexp match :
#   a = ins("AB = 12")
#   a.match('(.) = (.)')
#   left = a.str(1)
#   right = a.int(2)
class ins(str):
  def match(self, regex):
    self.__match = re.match(regex, self)
    return self.__match
  def str(self, idx):
    return self.__match.group(idx)
  def int(self, idx):
    return int(self.str(idx))

# Yields an instruction for each line of stdint
def inputs():
  for l in sys.stdin:
    yield ins(l.rstrip())
def input_file(filename):
  with open(filename) as f:
    for l in f.readlines():
      yield ins(l.rstrip())
