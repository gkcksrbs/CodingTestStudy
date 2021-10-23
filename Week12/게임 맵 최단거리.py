# 프로그래머스: 찾아라 프로그래밍 마에스터 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((0, 0))
    row, col = len(maps), len(maps[0])
    while q:
        now = q.popleft()
        for i in range(4):
            nx, ny = now[0] + dx[i], now[1] + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if nx == ny == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[now[0]][now[1]] + 1
                    q.append((nx, ny))
    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1]


if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))