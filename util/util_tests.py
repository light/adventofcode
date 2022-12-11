#!/usr/bin/env python3

import unittest
from util import *
from board import Board

class TestBoard(unittest.TestCase):
  def test_board_starts_empty(self):
    board = Board()
    self.assertEqual(board.w, 0)
    self.assertEqual(board.h, 0)
    with self.assertRaises(IndexError):
      board.get(0,0)
  def test_board_extends(self):
    board = Board()
    board.extend(2, 3)
    self.assertEqual(board.w, 2)
    self.assertEqual(board.h, 3)
  def test_board_get_bound_limited(self):
    board = Board()
    board.extend(2, 3)
    with self.assertRaises(IndexError):
      board.get(2, 3)
    with self.assertRaises(IndexError):
      board.get(2, 1)
    with self.assertRaises(IndexError):
      board.get(1, 3)
    with self.assertRaises(IndexError):
      board.get(-1, 1)
    with self.assertRaises(IndexError):
      board.get(1, -1)
  def test_board_extend(self):
    board = Board()
    board.extend(2, 3)
    self.assertEqual(board.w, 2)
    self.assertEqual(board.h, 3)
    self.assertEqual(board.get(1, 2), 0)
  def test_board_default_value(self):
    board = Board('#')
    board.extend(2, 3)
    self.assertEqual(board.get(1, 2), '#')
  def test_board_default_value_callable(self):
    board = Board(lambda: '#')
    board.extend(2, 3)
    self.assertEqual(board.get(1, 2), '#')
  def test_board_set_autoextend(self):
    board = Board()
    board.extend(1, 1)
    board.set(2, 3, 1)
    self.assertEqual(board.w, 3)
    self.assertEqual(board.h, 4)
    self.assertEqual(board.get(2, 3), 1)
  def test_board_set_negative(self):
    board = Board()
    board.extend(2, 3)
    with self.assertRaises(IndexError):
      board.set(-1, 1, 1)
    with self.assertRaises(IndexError):
      board.set(1, -1, 1)

if __name__ == '__main__':
    unittest.main()
