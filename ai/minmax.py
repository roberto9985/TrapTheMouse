import pygame
from copy import deepcopy
from entities.constants import BROWN, GREY, ROWS, COLS
from ai.heuristic import heuristicFunction

def minimax(tableTest, depth, max_turn):
    if depth == 0 or tableTest.winner() != "False":
        return heuristicFunction(tableTest), tableTest

    if max_turn:
        maxEval = float('-inf')
        best_move = None

        for move in get_available_moves(tableTest, GREY):
            evaluation = minimax(move, depth - 1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return (maxEval, best_move)

    else:
        minEval = float('inf')
        best_move = None

        for move in get_available_moves(tableTest, BROWN):
            evaluation = minimax(move, depth - 1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return (minEval, best_move)


def get_available_moves(Board, color):
    moves = []
    if color == GREY:
        if Board.mouseX % 2 == 0:
            for x in [-1, 0, 1]:
                for y in [-1, 0]:
                    if Board.board[Board.mouseX + x][Board.mouseY + y] == 0:
                        aux_board = deepcopy(Board)
                        aux_board.move((Board.mouseX + x), (Board.mouseY + y))
                        moves.append(aux_board)
            # Special case
            if Board.board[Board.mouseX][Board.mouseY + 1] == 0:
                aux_board = deepcopy(Board)
                aux_board.move((Board.mouseX), (Board.mouseY + 1))
                moves.append(aux_board)

        elif Board.mouseX % 2 == 1:
            for x in [-1, 0, 1]:
                for y in [0, 1]:
                    if Board.board[Board.mouseX + x][Board.mouseY + y] == 0:
                        aux_board = deepcopy(Board)
                        aux_board.move((Board.mouseX + x), (Board.mouseY + y))
                        moves.append(aux_board)
            # Special case
            if Board.board[Board.mouseX][Board.mouseY - 1] == 0:
                aux_board = deepcopy(Board)
                aux_board.move((Board.mouseX), (Board.mouseY - 1))
                moves.append(aux_board)

    else:
        for row in range(ROWS):
            for col in range(COLS):
                if Board.board[row][col] == 0:
                    aux_board = deepcopy(Board)
                    aux_board.add(row, col)
                    moves.append(aux_board)
    for move in moves:
        print(move.mouseX, move.mouseY)
    print('----------------------')
    return moves
