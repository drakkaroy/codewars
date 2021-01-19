def is_solved(board):
    
    lines = [board[0],
        board[1],
        board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if len([x for x in lines if x == [1, 1, 1]]) > 0:
        return 1
    elif len([x for x in lines if x == [2, 2, 2]]) > 0:
        return 2
    elif len([x for x in lines if 0 in x]) > 0:
        return -1
    else:
        return 0


# not yet finished -1
board1 = [[0, 0, 1],
          [0, 1, 2],
          [2, 1, 0]]

# winning row 1
board2 = [[1, 1, 1],
          [0, 2, 2],
          [0, 0, 0]]

# winning column 1
board3 = [[2, 1, 2],
          [2, 1, 1],
          [1, 1, 2]]

# draw 0
board4 = [[2, 1, 2],
          [2, 1, 1],
          [1, 2, 1]]

print(is_solved(board1))
print(is_solved(board2))
print(is_solved(board3))
print(is_solved(board4))

