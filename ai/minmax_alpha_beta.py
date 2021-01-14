from entities.constants import BROWN, GREY
from ai.heuristic import heuristic_function, get_available_moves


def minimax_alpha_beta(table_test, depth, alpha, beta, max_turn):
    """Summary or Description of the Function

        This function use the same algorithm mentioned in minmax.py but optimized with alpha-beta pruning.

    """
    if depth == 0 or table_test.winner != "False":
        return heuristic_function(table_test), depth

    if max_turn:
        max_eval = float('-inf')
        best_move = None

        for move in get_available_moves(table_test, GREY):
            evaluation = minimax_alpha_beta(move, depth - 1, alpha, beta, False)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None

        for move in get_available_moves(table_test, BROWN):
            evaluation = minimax_alpha_beta(move, depth - 1, alpha, beta, True)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval, best_move
