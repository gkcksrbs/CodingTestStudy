# 프로그래머스: 연습문제 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    dp = [[0, 0, 0, 0] for _ in range(len(land))]
    for i in range(len(land[0])):
        dp[0][i] = land[0][i]
    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j])
    return max(dp[-1])


if __name__ == '__main__':
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
