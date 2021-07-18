import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

m, n = map(int, input().split())
graph = []
dp = [[0]*n for i in range(m)]

for i in range(m):
    graph.append(list(map(int, input().split())))

dp[0][0] = 1

for k in range(5):
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            dp[i][j] = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[nx][ny] > graph[i][j]:
                        dp[i][j] += dp[nx][ny]

print(dp[-1][-1])