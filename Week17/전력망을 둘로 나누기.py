# 프로그래머스: 위클리 챌린지 전력망을 둘로 나누기
# https://programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque, Counter


def solution(n, wires):
    answer = int(1e9)
    length = len(wires)
    for i in range(length):
        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        for j in range(length):
            if i == j:
                continue
            a, b = wires[j][0], wires[j][1]
            graph[a].append(b)
            graph[b].append(a)
        q = deque()
        q.append(1)
        while q:
            now = q.popleft()
            visited[now] = True
            for num in graph[now]:
                if not visited[num]:
                    q.append(num)
        visited.pop(0)
        counter = list(Counter(visited).values())
        answer = min(answer, abs(counter[0] - counter[1]))
    return answer


if __name__ == '__main__':
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution(3, [[1, 2], [1, 3]]))
    print(solution())
