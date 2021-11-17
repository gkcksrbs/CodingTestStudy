# 프로그래머스: 동적계획법(Dynamic Programming) 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3
def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    for col, row in puddles:
        dp[row-1][col-1] = -1
    for i in range(m):
        if dp[0][i] == -1:
            break
        dp[0][i] = 1
    for i in range(n):
        if dp[i][0] == -1:
            break
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                continue
            if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                continue
            if dp[i-1][j] == -1:
                dp[i][j] = dp[i][j-1]
            elif dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])
    return dp[-1][-1] % 1000000007


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))
    print(solution(4, 3, []))