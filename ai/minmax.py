from entities.constants import BROWN, GREY
from ai.heuristic import heuristic_function, get_available_moves


def minimax(table_test, depth, max_turn):
    """Summary or Description of the Function

       This function use the minmax algorithm, in order to calculate which position is better for the mouse piece to win
        the game, based on the heuristic function.
         MinMax algorithm is clearly explained in the Wikipedia.

    """

    if depth == 0 or table_test.winner != "False":
        return heuristic_function(table_test), table_test

    if max_turn:
        max_eval = float('-inf')
        best_move = None

        for move in get_available_moves(table_test, GREY):
            evaluation = minimax(move, depth - 1, False)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None

        for move in get_available_moves(table_test, BROWN):
            evaluation = minimax(move, depth - 1, True)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move
