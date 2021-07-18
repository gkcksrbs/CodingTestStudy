# Baekjoon 1520 내리막 길
# 문제 : https://www.acmicpc.net/problem/1520
import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 그래프의 세로, 가로의 수 입력
m, n = map(int, input().split())
# 각 지역의 높이 그래프 생성
graph = []
# DP 배열 생성 및 초기화
dp = [[0]*n for i in range(m)]

# 각 지역의 높이 입력
for i in range(m):
    graph.append(list(map(int, input().split())))

# 맨 왼쪽 위 1로 초기화
dp[0][0] = 1

# 5번 순회
for k in range(5):
    for i in range(m):
        for j in range(n):
            # 맨 왼쪽 위는 무시
            if i == 0 and j == 0:
                continue
            # 탐색하는 지역에서 0으로 초기화한 후 상, 하, 좌, 우 지역에서 해당 지역으로 갈 수 있으면 더하기
            dp[i][j] = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[nx][ny] > graph[i][j]:
                        dp[i][j] += dp[nx][ny]

# 결과값 출력
print(dp[-1][-1])