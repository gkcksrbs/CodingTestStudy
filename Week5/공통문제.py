# 2021 카카오 채용연계형 인턴십 : 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302
from _collections import deque
# 상,하,좌,우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 너비우선탐색 알고리즘
def bfs(graph):
    person = []
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                person.append((i, j))

    for loc in person:
        # 방문 여부 리스트
        visited = [[False]*5 for i in range(5)]
        q = deque()
        q.append((loc[0], loc[1], 0))

        while q:
            x, y, dist = q.popleft()
            # 방문 처리
            visited[x][y] = True
            for d in range(4):
                # 현재에서의 상,하,좌,우 좌표
                nx, ny = x + dx[d], y + dy[d]
                # 그래프 범위 넘지 않고 이동거리가 2인 경우에만
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if graph[nx][ny] != 'X' and dist < 2 and not visited[nx][ny]:
                        q.append((nx, ny, dist+1))
                        if graph[nx][ny] == 'P':
                            return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        graph = []
        for data in place:
            graph.append(list(data))
        answer.append(bfs(graph))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))