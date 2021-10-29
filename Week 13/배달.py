# 프로그래머스: Summer/Winter Coding(~2018) 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq


def solution(N, road, K):
    INF = int(1e9)
    answer = 0
    graph = [[] for i in range(N+1)]
    distance = [INF] * (N+1)
    for start, end, cost in road:
        graph[start].append([end, cost])
        graph[end].append([start, cost])
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(	5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))