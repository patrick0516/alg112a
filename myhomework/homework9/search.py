def is_safe(board, row, col):
    # 檢查當前位置
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_eight_queens(board, row):
    n = len(board)

    if row == n:
        # 所有皇后都被成功放置
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            # 嘗試將皇后放在當前位置
            board[row] = col

            # 遞迴嘗試下一行
            solve_eight_queens(board, row + 1)

            # 回朔、嘗試下一個位置
            board[row] = -1

# 初始化一个8×8的棋盤，-1表示空格
initial_board = [-1] * 8

# 從遞0行開始嘗試擺放皇后
solve_eight_queens(initial_board, 0)
