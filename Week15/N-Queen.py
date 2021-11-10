# 프로그래머스: 연습문제 N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952
def solution(n):
    board = [[0]*n for _ in range(n)]
    answer = n_queen(0, board)
    return answer


def n_queen(row, board):
    count = 0
    if row == len(board)-1:
        for i in range(len(board)):
            if not is_attack(row, i, board):
                count += 1
    else:
        for i in range(len(board)):
            if not is_attack(row, i, board):
                board[row][i] = 1
                count += n_queen(row+1, board)
                board[row][i] = 0
    return count


def is_attack(row, col, board):
    for i in range(row):
        if board[i][col] == 1:
            return True
    r, c = row-1, col-1
    while 0 <= r < len(board) and (0 <= c < len(board)):
        if board[r][c] == 1:
            return True
        r -= 1
        c -= 1
    r, c = row-1, col+1
    while 0 <= r < len(board) and 0 <= c < len(board):
        if board[r][c] == 1:
            return True
        r -= 1
        c += 1
    return False


if __name__ == '__main__':
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))
    print(solution(9))
    print(solution(10))
    print(solution(11))
    print(solution(12))
