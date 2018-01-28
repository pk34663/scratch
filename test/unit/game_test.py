import unittest
from app import game

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = game.Board(5,5)

    def test_move_right_from_north(self):
        self.board.piece.set_direction(game.Direction.NORTH)
        self.board.piece.move("R")

        self.assertEqual(game.Direction.EAST, self.board.piece.direction)

    def test_move_right_from_south(self):
        self.board.piece.set_direction(game.Direction.SOUTH)
        self.board.piece.move("R")

        self.assertEqual(game.Direction.WEST, self.board.piece.direction)

    def test_move_right_from_west(self):
        self.board.piece.set_direction(game.Direction.WEST)
        self.board.piece.move("R")

        self.assertEqual(game.Direction.NORTH, self.board.piece.direction)

    def test_move_right_from_east(self):
        self.board.piece.set_direction(game.Direction.EAST)
        self.board.piece.move("R")

        self.assertEqual(game.Direction.SOUTH, self.board.piece.direction)

    def test_move_left_from_north(self):
        self.board.piece.set_direction(game.Direction.NORTH)
        self.board.piece.move("L")

        self.assertEqual(game.Direction.WEST, self.board.piece.direction)

    def test_move_left_from_south(self):
        self.board.piece.set_direction(game.Direction.SOUTH)
        self.board.piece.move("L")

        self.assertEqual(game.Direction.EAST, self.board.piece.direction)

    def test_move_left_from_west(self):
        self.board.piece.set_direction(game.Direction.WEST)
        self.board.piece.move("L")

        self.assertEqual(game.Direction.SOUTH, self.board.piece.direction)

    def test_move_off_lhs_board(self):
        self.board.piece.set_direction(game.Direction.WEST)
        self.board.movePiece("MMMMMM")
        self.assertEqual(self.board.piece.x, 0)

    def test_move_off_rhs_board(self):
        self.board.piece.set_direction(game.Direction.EAST)
        self.board.movePiece("MMMMMM")
        self.assertEqual(self.board.piece.x, 4)
         
    def test_move_off_top_board(self):
        self.board.piece.set_direction(game.Direction.NORTH)
        self.board.movePiece("MMMMMM")
        self.assertEqual(self.board.piece.y, 4)

    def test_move_off_bottom_board(self):
        self.board.piece.set_direction(game.Direction.SOUTH)
        self.board.movePiece("MMMMMM")
        self.assertEqual(self.board.piece.x, 0)

    def test_move_series_one(self):
        self.board.piece.set_direction(game.Direction.NORTH)
        location = self.board.movePiece("MRMLMRM")

        self.assertEqual("2 2 E", location)

    def test_move_series_two(self):
        self.board.piece.set_direction(game.Direction.NORTH)
        location = self.board.movePiece("RMMMLMM")

        self.assertEqual("3 2 N", location)

    def test_move_series_three(self):
        self.board.piece.set_direction(game.Direction.NORTH)
        location = self.board.movePiece("MMMMM")

        self.assertEqual("0 4 N", location)

if __name__ == "__main__":
    unittest.main()
