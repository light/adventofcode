#!/usr/bin/env python3

import unittest
from util import *
from board import Board

class TestBoard(unittest.TestCase):
  def test_board_starts_empty(self):
    board = Board()
    self.assertEqual(board.w, 0)
    self.assertEqual(board.h, 0)
    self.assertEqual(board.x0, 0)
    self.assertEqual(board.y0, 0)
    with self.assertRaises(IndexError):
      board.get(0,0)
  def test_board_extend(self):
    board = Board()
    board.extend(2, 3)
    self.assertEqual(board.w, 2)
    self.assertEqual(board.h, 3)
    self.assertEqual(board.x0, 0)
    self.assertEqual(board.y0, 0)
  def test_board_extend_shift(self):
    board = Board('.')
    board.set(1, 2, '#')
    self.assertEqual(board.get(1, 2), '#')
    board.extend_shift(20, 30, 40, 50)
    self.assertEqual(board.w, 62)
    self.assertEqual(board.h, 83)
    self.assertEqual(board.x0, 0)
    self.assertEqual(board.y0, 0)
    self.assertEqual(board.get(1, 2), '.')
    self.assertEqual(board.get(21, 32), '#')
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
  def test_board_set(self):
    board = Board('.')
    board.set(1, 0, '#')
    board.set(0, 1, 'S')
    self.assertEqual(board.get(1, 0), '#')
    self.assertEqual(board.get(0, 1), 'S')
  def test_board_set_negative_origin(self):
    board = Board('.')
    board.extend(3, 3)
    board.shift(-2, -2)
    board.set(1, 1, '#')
  def test_board_set_autoextend(self):
    board = Board()
    board.extend(1, 1)
    board.set(2, 3, 1)
    self.assertEqual(board.w, 3)
    self.assertEqual(board.h, 4)
    self.assertEqual(board.x0, 0)
    self.assertEqual(board.y0, 0)
    self.assertEqual(board.get(2, 3), 1)
  def test_board_shift(self):
    board = Board('.')
    board.set(0, 0, '#')
    board.set(1, 0, 'S')
    board.shift(30, 20)
    self.assertEqual(board.w, 2)
    self.assertEqual(board.h, 1)
    self.assertEqual(board.x0, 30)
    self.assertEqual(board.y0, 20)
    self.assertEqual(board.get(30, 20), '#')
    self.assertEqual(board.get(31, 20), 'S')
  def test_board_shift_negative(self):
    board = Board('.')
    board.set(1, 0, '#')
    board.set(0, 1, 'S')
    board.shift(-30, -20)
    self.assertEqual(board.w, 2)
    self.assertEqual(board.h, 2)
    self.assertEqual(board.x0, -30)
    self.assertEqual(board.y0, -20)
    self.assertEqual(board.get(-29, -20), '#')
    self.assertEqual(board.get(-30, -19), 'S')
  def test_board_set_autoextend_negative(self):
    board = Board('.')
    board.extend(2, 3)
    board.set(-1, 1, '#')
    self.assertEqual(board.w, 3)
    self.assertEqual(board.h, 3)
    self.assertEqual(board.x0, -1)
    self.assertEqual(board.y0, 0)
    self.assertEqual(board.get(-1, 1), '#')
    board.set(1, -1, '#')
    self.assertEqual(board.w, 3)
    self.assertEqual(board.h, 4)
    self.assertEqual(board.x0, -1)
    self.assertEqual(board.y0, -1)
    self.assertEqual(board.get(1, -1), '#')

if __name__ == '__main__':
    unittest.main()
