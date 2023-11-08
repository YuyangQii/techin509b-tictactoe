import unittest
import logic


class TestLogic(unittest.TestCase):
       
       def test_empty_board(self):
        # Test empty board
        empty_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), empty_board)

       def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!

    # Test when there is no winner
        board_no_winner = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board_no_winner), None)

    # Test when 'X' wins 
        board_x_winner= [
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
            ['O', 'O', None],
        ]
        self.assertEqual(logic.get_winner(board_x_winner), 'X')

    # Test when 'O' wins 
        board_o_winner = [
            ['X', 'O', None],
            ['X', 'O', 'X'],
            [None, 'O', None],
        ]
        self.assertEqual(logic.get_winner(board_o_winner), 'O')

def test_other_player(self):
    # Test that the other player is returned correctly
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

if __name__ == '__main__':
    unittest.main()
