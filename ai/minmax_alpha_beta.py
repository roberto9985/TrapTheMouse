import pygame
from copy import deepcopy
from entities.constants import BROWN, GREY, ROWS, COLS

def heuristicFunction(copyTable):
    curr_x = copyTable.mouseX 
    curr_y = copyTable.mouseY
    min_list = []
    count_up, count_down, count_left, count_right, count_up_left, count_up_right, count_down_left, count_down_right = 0,0,0,0,0,0,0,0
    
    for up in range(curr_x):
        if copyTable.board[up][curr_y] == 0:
                count_up += 1
        else:
            count_up = 0
            # float('inf')
            break
    # min_list.append(count_up)
    
    for down in range(curr_x + 1, ROWS):
        if copyTable.board[down][curr_y] == 0:
                count_down += 1
        else:
            count_down = 0 
            # float('inf')
            break
    # min_list.append(count_down)

    for left in range(curr_y):
        if copyTable.board[curr_y][left] == 0:
                count_left += 1
        else:
            count_left = 0
            # float('inf')
            break
    # min_list.append(count_left)

    for right in range(curr_y + 1, COLS):
        if copyTable.board[curr_x][right] == 0:
                count_right += 1
        else:
            count_right = 0 
            # float('inf')
            break
    # min_list.append(count_right)
    
    for up_left in range(1, ROWS):
        if copyTable.board[curr_x - up_left][curr_y - up_left] == 0:
                count_up_left += 1
        else:
            count_up_left = 0 
            # float('inf')
            break
        if (curr_x - up_left) == 0 or (curr_y - up_left) == 0:
            break
    # min_list.append(count_up_left)

    for up_right in range(1, ROWS):
        if (curr_x - up_right ) == 0 or (curr_y + up_right) == COLS:
            break

        if copyTable.board[curr_x - up_right][curr_y + up_right] == 0:
                count_up_right += 1
        else:
            count_up_right = 0
            # float('inf')
            break
    # min_list.append(count_up_right)

    for down_left in range(1, ROWS):
        if (down_left + curr_x) == ROWS or (curr_y - down_left) == 0:
            break

        if copyTable.board[curr_x + down_left][curr_y - down_left] == 0:
                count_down_left += 1
        else:
            count_down_left = 0
            # float('inf')
            break
    # min_list.append(count_down_left)

    for down_right in range(1, ROWS):
        if (down_right + curr_x) == ROWS or (down_right + curr_y) == COLS:
            break
        
        if copyTable.board[curr_x + down_right][curr_y + down_right] == 0:
                count_down_right += 1
        else:
            count_down_right = 0
            # float('inf')
            break
    # min_list.append(count_down_right)
    sum_available = count_up + count_down + count_left + count_right + count_up_left + count_up_right + count_down_left + count_down_right
    return sum_available


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
                    aux_board.add(row,col)
                    moves.append(aux_board)
    return moves
