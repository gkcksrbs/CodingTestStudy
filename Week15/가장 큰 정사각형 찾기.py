# 프로그래머스: 연습문제 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    answer = 1
    row, col = len(board), len(board[0])
    if len(board) == 1:
        return 1
    dp = [[0]*col for _ in range(row)]
    for i in range(row):
        dp[i][0] = board[i][0]
    for j in range(col):
        dp[0][j] = board[0][j]
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                if dp[i][j] > answer:
                    answer = dp[i][j]
    return answer**2


if __name__ == '__main__':
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
    print(solution([[0,0,1,1],[1,1,1,1]]))
    print(solution([[1,0],[0,0]]))