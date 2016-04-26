import crazyhouse_engine
from nose.tools import assert_raises
from nose.tools import assert_equal
from nose.tools import raises

def test_convert_coordinates_valid():
  result = crazyhouse_engine.State.convert_coordinates("e6")
  assert_equal(result, (4, 5))
  result = crazyhouse_engine.State.convert_coordinates("a1")
  assert_equal(result, (0, 0))
  result = crazyhouse_engine.State.convert_coordinates("h8")
  assert_equal(result, (7, 7))

def test_convert_coordinates_upper_case():
  result = crazyhouse_engine.State.convert_coordinates("H8")
  assert_equal(result, (7, 7))

@raises(ValueError)
def test_convert_coordinates_not_two_characters():
  result = crazyhouse_engine.State.convert_coordinates("foo")

@raises(ValueError)
def test_convert_coordinates_invalid_column():
  result = crazyhouse_engine.State.convert_coordinates("i8")

@raises(ValueError)
def test_convert_coordinates_invalid_row():
  result = crazyhouse_engine.State.convert_coordinates("a9")

@raises(ValueError)
def test_convert_coordinates_invalid_column_numeric():
  result = crazyhouse_engine.State.convert_coordinates("88")

@raises(ValueError)
def test_convert_coordinates_invalid_row_alphabetic():
  result = crazyhouse_engine.State.convert_coordinates("hh")

def test_place_piece():
  state = crazyhouse_engine.State()
  state.place_piece("e6", crazyhouse_engine.Piece.WK)
  assert_equal(state.board[4][5], crazyhouse_engine.Piece.WK)

def test_initialize():
  state = crazyhouse_engine.State()
  state.initialize()
  assert_equal(state.board[0][0], crazyhouse_engine.Piece.WR)
  assert_equal(state.board[6][1], crazyhouse_engine.Piece.WP)
  assert_equal(state.board[7][7], crazyhouse_engine.Piece.BR)
  assert_equal(state.board[4][6], crazyhouse_engine.Piece.BP)


