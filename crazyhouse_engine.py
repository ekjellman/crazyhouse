from enum import Enum

WHITE = 1
BLACK = -1

class Piece(Enum):
  WP = 1
  WN = 2
  WB = 3
  WR = 4
  WQ = 5
  WK = 6
  BP = -1
  BN = -2
  BB = -3
  BR = -4
  BQ = -5
  BK = -6

class State(object):
  def __init__(self):
    self.board = [[0] * 8 for x in range(8)]
    self.turn = WHITE
    # white king-side, white queen-side, black king-side, black queen-side
    self.castling = [0, 0, 0, 0]
    # white, black
    self.pieces_in_hand = [[], []]
    self.en_passant = None

  def initialize(self):
    self.board = [[0] * 8 for x in range(8)]
    self.turn = WHITE
    self.castling = [1, 1, 1, 1]
    self.pieces_in_hand = [[], []]
    self.en_passant = None
    pieces = [("a1", Piece.WR),
              ("b1", Piece.WN),
              ("c1", Piece.WB),
              ("d1", Piece.WQ),
              ("e1", Piece.WK),
              ("f1", Piece.WB),
              ("g1", Piece.WN),
              ("h1", Piece.WR),
              ("a2", Piece.WP),
              ("b2", Piece.WP),
              ("c2", Piece.WP),
              ("d2", Piece.WP),
              ("e2", Piece.WP),
              ("f2", Piece.WP),
              ("g2", Piece.WP),
              ("h2", Piece.WP),
              ("a7", Piece.BP),
              ("b7", Piece.BP),
              ("c7", Piece.BP),
              ("d7", Piece.BP),
              ("e7", Piece.BP),
              ("f7", Piece.BP),
              ("g7", Piece.BP),
              ("h7", Piece.BP),
              ("a8", Piece.BR),
              ("b8", Piece.BN),
              ("c8", Piece.BB),
              ("d8", Piece.BQ),
              ("e8", Piece.BK),
              ("f8", Piece.BB),
              ("g8", Piece.BN),
              ("h8", Piece.BR)]
    for piece in pieces:
      self.place_piece(*piece)

  def place_piece(self, coord, piece):
    coords = self.convert_coordinates(coord)
    self.board[coords[0]][coords[1]] = piece

  @staticmethod
  def convert_coordinates(coord):
    """Converts names like "e6" into coordinates for the board (4, 5)"""
    if len(coord) != 2:
       raise ValueError("Invalid coordinate %s" % coord)
    column = ord(coord.lower()[0]) - 97
    if not 0 <= column <= 7:
       raise ValueError("Invalid coordinate %s" % coord)
    try:
       row = int(coord[1]) - 1
    except ValueError:
       raise ValueError("Invalid coordinate %s" % coord)
    if not 0 <= row <= 7:
       raise ValueError("Invalid coordinate %s" % coord)
    return (column, row)

  @staticmethod
  def coord(coord):
    """convenience method"""
    return convert_coordinates(coord)
