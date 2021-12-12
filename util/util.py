#!/usr/bin/env python3

import sys

def print_res(msg, val, exp_arg):
  expected = int(sys.argv[exp_arg]) if len(sys.argv) > exp_arg else None
  if expected:
    okko = "\033[92mOK!\033[0m" if val == expected else f"\033[91mKO!\033[0m (expected {expected})"
    print(msg, val, okko)
  else:
    print(msg, val)
