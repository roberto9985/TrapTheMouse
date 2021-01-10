import pygame
from copy import deepcopy
from entities.constants import BROWN, GREY, ROWS, COLS
from ai.heuristic import heuristicFunction

def minimaxAlpha_Beta(tableTest, depth, alpha, beta, max_turn):
    if depth == 0 or tableTest.winner() != "False":
        return heuristicFunction(tableTest),depth
    
    if max_turn:
        maxEval = float('-inf')
        best_move = None
        
        for move in get_available_moves(tableTest, GREY):
            evaluation = minimaxAlpha_Beta(move, depth-1, alpha, beta, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
            
        return (maxEval, best_move)
    else:
        minEval = float('inf')
        best_move = None

        for move in get_available_moves(tableTest, BROWN):
            evaluation = minimaxAlpha_Beta(move, depth-1, alpha, beta, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            beta = min(beta, minEval)
            if beta <= alpha:
                break 
        return (minEval, best_move)


def get_available_moves(Board, color):
    moves = []
    if color == GREY:
        for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if(Board.board[Board.mouseX + x][Board.mouseY + y]) == 0:
                        aux_board = deepcopy(Board)
                        aux_board.move((Board.mouseX + x) , (Board.mouseY + y))
                        moves.append(aux_board)
    else:
        for row in range(ROWS):
            for col in range(COLS):
                if Board.board[row][col] == 0:
                    aux_board = deepcopy(Board)
                    aux_board.add(row, col)
                    moves.append(aux_board)
    return moves
