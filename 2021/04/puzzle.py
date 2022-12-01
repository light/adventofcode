#!/usr/bin/env python3

import sys

inputs = sys.stdin.read().split("\n\n")
draws = inputs.pop(0).split(",")

def parse_board(input):
  nums = [l.split() for l in input.splitlines()]
  return {
    "nums": nums,
    "got": [[False] * len(nums[0])for i in range(len(nums))]
  }
  nums = lines = input.splitlines()
  return [l.split() for l in input.splitlines()]
boards = [parse_board(i) for i in inputs]

def play_bingo(board, drawn_num):
  for i, l in enumerate(board["nums"]):
    for j, num in enumerate(l):
      if num == drawn_num:
        board['got'][i][j] = True
        return
def is_winning(board):
  n = len(board["got"])
  for i in range(0, n):
    got_x = got_y = True
    for j in range(0, n):
      got_x = got_x and board["got"][i][j]
      got_y = got_y and board["got"][j][i]
    if got_x or got_y:
      return True
  return False
def find_winners():
  winners = []
  for draw in draws:
    for board in boards:
      play_bingo(board, draw)
    for board in boards.copy():
      if(is_winning(board)):
        boards.remove(board)
        winners.append((board, draw))
  return winners
def get_score(board, draw):
  s = 0
  for i, l in enumerate(board["nums"]):
    for j, num in enumerate(l):
      if not board['got'][i][j]:
        s += int(board['nums'][i][j])
  return s * int(draw)

winners = find_winners()
print("First:", get_score(*winners[0]))
print("Last:", get_score(*winners[-1]))
